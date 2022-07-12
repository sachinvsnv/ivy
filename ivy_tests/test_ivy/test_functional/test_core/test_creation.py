"""Collection of tests for creation functions."""

# global

import numpy as np
from hypothesis import given, strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
import ivy.functional.backends.numpy as ivy_np
import hypothesis.extra.numpy as hnp


# native_array
@given(
    dtype_and_x=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
        shared_dtype=True,
    ),
    as_variable=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="native_array"),
    native_array=st.booleans(),
    instance_method=st.booleans(),
)
def test_native_array(
    dtype_and_x,
    as_variable,
    num_positional_args,
    native_array,
    instance_method,
    fw,
    device,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        dtype,
        as_variable,
        False,
        num_positional_args,
        native_array,
        False,
        instance_method,
        fw,
        "native_array",
        x=np.asarray(x),
        dtype=dtype,
        device=device,
    )


# linspace
@given(
    dtype_and_start_stop=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        allow_inf=False,
        min_num_dims=1,
        max_num_dims=1,
        min_dim_size=2,
        max_dim_size=2,
    ),
    num=st.integers(1, 5),
    axis=st.none(),
    num_positional_args=helpers.num_positional_args(fn_name="linspace"),
)
def test_linspace(
    dtype_and_start_stop,
    num,
    axis,
    device,
    num_positional_args,
    fw,
):
    dtype, start_stop = dtype_and_start_stop
    helpers.test_function(
        dtype,
        False,
        False,
        num_positional_args,
        False,
        False,
        False,
        fw,
        "linspace",
        start=start_stop[0],
        stop=start_stop[1],
        num=num,
        axis=axis,
        device=device,
    )


# logspace
@given(
    dtype_and_start_stop=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        allow_inf=False,
        min_num_dims=1,
        max_num_dims=1,
        min_dim_size=2,
        max_dim_size=2,
    ),
    num=st.integers(1, 5),
    base=st.floats(min_value=0.1, max_value=10.0),
    axis=st.none(),
    num_positional_args=helpers.num_positional_args(fn_name="logspace"),
)
def test_logspace(
    dtype_and_start_stop,
    num,
    base,
    axis,
    device,
    num_positional_args,
    fw,
):
    dtype, start_stop = dtype_and_start_stop
    helpers.test_function(
        dtype,
        False,
        False,
        num_positional_args,
        False,
        False,
        False,
        fw,
        "logspace",
        test_rtol=(1,),  # if its less then one it'll test for inf
        test_atol=(1e-06,),
        test_values=True,
        start=start_stop[0],
        stop=start_stop[1],
        num=num,
        base=base,
        axis=axis,
        device=device,
    )


# arange
@given(
    start=st.integers(0, 5),
    stop=st.integers(0, 5) | st.none(),
    step=st.integers(-5, 5).filter(lambda x: True if x != 0 else False),
    dtype=st.sampled_from(ivy_np.valid_int_dtypes),
    num_positional_args=helpers.num_positional_args(fn_name="arange"),
    with_out=st.booleans(),
)
def test_arange(
    start,
    stop,
    step,
    dtype,
    device,
    num_positional_args,
    with_out,
    fw,
):
    helpers.test_function(
        dtype,
        False,
        with_out,
        num_positional_args,
        False,
        False,
        False,
        fw,
        "arange",
        start=start,
        stop=stop,
        step=step,
        dtype=dtype,
        device=device,
    )


# asarray
@given(
    dtype_and_x=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        min_num_dims=0,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=5,
    ),
    as_variable=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="asarray"),
    native_array=st.booleans(),
    instance_method=st.booleans(),
)
def test_asarray(
    dtype_and_x,
    device,
    as_variable,
    num_positional_args,
    native_array,
    instance_method,
    fw,
):
    dtype, x = dtype_and_x

    if instance_method:
        x = np.asarray(x)

    helpers.test_function(
        dtype,
        as_variable,
        False,
        num_positional_args,
        native_array,
        False,
        instance_method,
        fw,
        "asarray",
        object_in=x,
        dtype=dtype,
        device=device,
    )


# empty
@given(
    shape=helpers.get_shape(
        allow_none=False,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
    ),
    dtype=st.sampled_from(ivy_np.valid_numeric_dtypes),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="empty"),
)
def test_empty(
    shape,
    dtype,
    device,
    with_out,
    num_positional_args,
    fw,
):

    helpers.test_function(
        dtype,
        False,
        with_out,
        num_positional_args,
        False,
        False,
        False,
        fw,
        "empty",
        shape=shape,
        dtype=dtype,
        device=device,
    )


# empty_like
@given(
    dtype_and_x=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=5,
    ),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="empty_like"),
    native_array=st.booleans(),
    instance_method=st.booleans(),
)
def test_empty_like(
    dtype_and_x,
    device,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    instance_method,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        dtype,
        as_variable,
        with_out,
        num_positional_args,
        native_array,
        False,
        instance_method,
        fw,
        "empty_like",
        x=np.asarray(x),
        dtype=dtype,
        device=device,
    )


# eye
@given(
    n_rows=st.integers(min_value=0, max_value=5),
    n_cols=st.none() | st.integers(min_value=0, max_value=5),
    k=st.integers(min_value=-5, max_value=5),
    dtype=st.sampled_from(ivy_np.valid_int_dtypes),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="eye"),
)
def test_eye(
    n_rows,
    n_cols,
    k,
    dtype,
    device,
    as_variable,
    with_out,
    num_positional_args,
    fw,
):

    helpers.test_function(
        dtype,
        as_variable,
        with_out,
        num_positional_args,
        False,
        False,
        False,
        fw,
        "eye",
        n_rows=n_rows,
        n_cols=n_cols,
        k=k,
        dtype=dtype,
        device=device,
    )


# from_dlpack
@given(
    dtype_and_x=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=5,
    ),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=st.integers(0, 1),
    native_array=st.booleans(),
    container=st.booleans(),
    instance_method=st.booleans(),
)
def test_from_dlpack(
    dtype_and_x,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    container,
    instance_method,
    fw,
):
    if fw == "tensorflow" or fw == "jax":  # not working at time of commit
        return

    dtype, x = dtype_and_x
    helpers.test_function(
        dtype,
        as_variable,
        with_out,
        num_positional_args,
        native_array,
        False,
        instance_method,
        fw,
        "from_dlpack",
        x=np.asarray(x),
    )


# full
@given(
    shape=helpers.get_shape(
        allow_none=False,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
    ),
    fill_value=st.integers(0, 5) | st.floats(0.0, 5.0),
    dtype=st.sampled_from(ivy_np.valid_numeric_dtypes),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="full"),
)
def test_full(
    shape,
    fill_value,
    dtype,
    with_out,
    device,
    num_positional_args,
    fw,
):

    if type(fill_value) == float and dtype in ivy_np.valid_int_dtypes:
        return

    helpers.test_function(
        dtype,
        False,
        with_out,
        num_positional_args,
        False,
        False,
        False,
        fw,
        "full",
        shape=shape,
        fill_value=fill_value,
        dtype=dtype,
        device=device,
    )


# full_like()
@given(
    dtype_and_x=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=5,
    ),
    fill_value=st.integers(-5, 5) | st.floats(-5, 5),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="full_like"),
    native_array=st.booleans(),
    instance_method=st.booleans(),
)
def test_full_like(
    dtype_and_x,
    device,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    instance_method,
    fw,
    fill_value,
):
    dtype, x = dtype_and_x

    helpers.test_function(
        dtype,
        as_variable,
        with_out,
        num_positional_args,
        native_array,
        False,
        instance_method,
        fw,
        "full_like",
        x=np.asarray(x),
        fill_value=fill_value,
        dtype=dtype,
        device=device,
    )


# meshgrid


# allows for arrays of all 1d and same dtype
array_shape = st.shared(
    st.lists(st.integers(min_value=1, max_value=5), min_size=1, max_size=1)
)
dtype_shared = st.shared(st.sampled_from(ivy_np.valid_numeric_dtypes))


@given(
    arrays=st.lists(
        hnp.arrays(dtype=dtype_shared, shape=array_shape), min_size=1, max_size=3
    ),
    indexing=st.sampled_from(["xy", "ij"]),
    dtype=dtype_shared,
)
def test_meshgrid(
    arrays,
    indexing,
    dtype,
    fw,
):

    if fw == "torch" and dtype == "uint16" or "uint32":
        return

    kw = {}
    i = 0
    for x_ in arrays:
        kw["x{}".format(i)] = x_
        i += 1

    num_positional_args = len(arrays)

    helpers.test_function(
        dtype,
        False,
        False,
        num_positional_args,
        False,
        False,
        False,
        fw,
        "meshgrid",
        **kw,
        indexing=indexing
    )


# ones
@given(
    shape=helpers.get_shape(
        allow_none=False,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
    ),
    dtype=st.sampled_from(ivy_np.valid_numeric_dtypes),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="ones"),
)
def test_ones(
    shape,
    dtype,
    with_out,
    device,
    num_positional_args,
    fw,
):
    helpers.test_function(
        dtype,
        False,
        with_out,
        num_positional_args,
        False,
        False,
        False,
        fw,
        "ones",
        shape=shape,
        dtype=dtype,
        device=device,
    )


# ones_like
@given(
    dtype_and_x=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=5,
    ),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=st.integers(0, 1),
    native_array=st.booleans(),
    instance_method=st.booleans(),
)
def test_ones_like(
    dtype_and_x,
    device,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    instance_method,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        dtype,
        as_variable,
        with_out,
        num_positional_args,
        native_array,
        False,
        instance_method,
        fw,
        "ones_like",
        x=np.asarray(x, dtype=dtype),
        dtype=dtype,
        device=device,
    )


# tril
@given(
    dtype_and_x=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        min_num_dims=2,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
    ),
    k=st.integers(-5, 5),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="tril"),
    native_array=st.booleans(),
    instance_method=st.booleans(),
)
def test_tril(
    dtype_and_x,
    k,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    instance_method,
    fw,
):
    dtype, x = dtype_and_x

    helpers.test_function(
        dtype,
        as_variable,
        with_out,
        num_positional_args,
        native_array,
        False,
        instance_method,
        fw,
        "tril",
        x=np.asarray(x),
        k=k,
    )


# triu
@given(
    dtype_and_x=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        min_num_dims=2,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
    ),
    k=st.integers(-5, 5),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="triu"),
    native_array=st.booleans(),
    instance_method=st.booleans(),
)
def test_triu(
    dtype_and_x,
    k,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    instance_method,
    fw,
):
    dtype, x = dtype_and_x

    helpers.test_function(
        dtype,
        as_variable,
        with_out,
        num_positional_args,
        native_array,
        False,
        instance_method,
        fw,
        "triu",
        x=np.asarray(x),
        k=k,
    )


# zeros
@given(
    shape=helpers.get_shape(
        allow_none=False,
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
    ),
    dtype=st.sampled_from(ivy_np.valid_int_dtypes),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="zeros"),
)
def test_zeros(
    shape,
    dtype,
    device,
    with_out,
    num_positional_args,
    fw,
):
    helpers.test_function(
        dtype,
        False,
        with_out,
        num_positional_args,
        False,
        False,
        False,
        fw,
        "zeros",
        shape=shape,
        dtype=dtype,
        device=device,
    )


# zeros_like
@given(
    dtype_and_x=helpers.dtype_and_values(
        ivy_np.valid_numeric_dtypes,
        n_arrays=1,
        min_num_dims=2,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
    ),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="zeros_like"),
    native_array=st.booleans(),
    instance_method=st.booleans(),
)
def test_zeros_like(
    dtype_and_x,
    device,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    instance_method,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        dtype,
        as_variable,
        with_out,
        num_positional_args,
        native_array,
        False,
        instance_method,
        fw,
        "zeros_like",
        x=np.asarray(x, dtype=dtype),
        dtype=dtype,
        device=device,
    )
