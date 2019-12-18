import altair as alt
from vega_datasets import data

source = data.iris()

a = alt.Chart(source).transform_fold(
    ['petalWidth',
     'petalLength',
     'sepalWidth',
     'sepalLength'],
    as_ = ['Measurement_type', 'value']
).transform_density(
    density='value',
    bandwidth=0.5,
    groupby=['Measurement_type'],
    extent= [0, 8]
).mark_area(opacity=0.5).encode(
    alt.X('value:Q'),
    alt.Y('density:Q'),
    alt.Color('Measurement_type:N')
)

b = alt.Chart(source).transform_fold(
    ['petalWidth',
     'petalLength',
     'sepalWidth',
     'sepalLength'],
    as_ = ['Measurement_type', 'value']
).transform_density(
    density='value',
    bandwidth=0.5,
    groupby=['Measurement_type'],
    extent= [0, 8]
).mark_line(opacity=1).encode(
    alt.X('value:Q'),
    alt.Y('density:Q'),
    alt.Color('Measurement_type:N')
)

a+b
