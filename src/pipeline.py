import logging
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s][%(levelname)s] %(message)s'
)

type2col = {
    'HKQuantityTypeIdentifierStepCount': 'step',
    'HKQuantityTypeIdentifierDistanceWalkingRunning': 'distance',
    'HKQuantityTypeIdentifierFlightsClimbed': 'floor'
}
col2dtype = {
    'step': int,
    'distance': float,
    'floor': int
}

def load_raw_data(fn):
    return pd.read_xml(
        open(fn, 'r'),
        xpath="//Record"
    )

def parse_date_cols(df):
    cols = ['creationDate','startDate','endDate']
    for col in cols:
        df[col] = pd.to_datetime(df[col])
    return df

def add_middleDate_col(df):
    df['middleDate'] = df['startDate'] + (df['endDate'] - df['startDate']) / 2
    return df

def skip_first_day(df):
    # Assuming the index to be in datetime format
    # Skip the first day of data because of missing data
    return df[df.index >= '2018-08-24']

def process_cols(df, target_cols: dict, col2dtype: dict, freq='D'):
    """
    You specify the target columns to include in the output and the frequency of the resampling.

    `target_cols` must be a dict mapping the desired column names to values of the column `type`.
    """
    data = {}
    for type_, label in target_cols.items():
        data[label] = \
            df[df.type == type_] \
            .rename(columns={'value': label}) \
            .loc[:, label] \
            .astype(col2dtype[label]) \
            .resample(freq) \
            .sum() \
            .to_frame()
    return pd.concat(data.values(), axis=1)

def pipeline(in_fn, freq='D'):
    logging.info(f'Loading raw data from {in_fn}')
    df = load_raw_data(in_fn)
    logging.info('Parsing datetime columns')
    df = parse_date_cols(df)
    logging.info('Adding middleDate column')
    df = add_middleDate_col(df)
    df.set_index('middleDate', inplace=True)
    logging.info('Skipping the first day of data')
    df = skip_first_day(df)
    logging.info(f'Resampling data with freq={freq}')
    df = process_cols(
        df, 
        type2col, 
        col2dtype,
        freq
    )
    
    return df

if __name__ == '__main__':

    from argparse import ArgumentParser
    parser = ArgumentParser(usage='python -m src.pipeline -i <in_data> -o <out_data> -f <freq>')
    parser.add_argument('-i', '--in_fn', type=str, help='Path to the input data file')
    parser.add_argument('-o', '--out_fn', type=str, help='Path to the output data file')
    parser.add_argument('-f', '--freq', type=str, default='D', help='Resampling frequency. Valid values are those compatible with pandas.DataFrame.resample method. See https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html')
    args = parser.parse_args()

    df = pipeline(args.in_fn, args.freq)
    logging.info(f'Saving processed data to {args.out_fn}')
    df.to_csv(args.out_fn, index=True)