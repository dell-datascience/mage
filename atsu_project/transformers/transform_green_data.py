import re
import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
      
    print(f"\n*** Pre: missing passenger count: {data['passenger_count'].isin([0]).sum()} and missing trip_distance: {data['trip_distance'].isin([0]).sum()}")
    data = data[data['passenger_count'] != 0]
    data = data[data['trip_distance']   != 0]

    print(f"\n*** Pre: missing passenger count: {data['passenger_count'].isin([0]).sum()} and missing trip_distance: {data['trip_distance'].isin([0]).sum()}")

    # data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.strftime('%Y-%m-%d')
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    data.columns = [camel_to_snake(col) for col in data.columns]

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert 'vendor_id' in output.columns, 'The output does not contain the expected columns'
    assert output['passenger_count'].isin([0]).sum() == 0, 'Passenger_count contains missing passenger counts'
    assert output['trip_distance'].isin([0]).sum() == 0, 'Trip_distance contains missing trip distances'