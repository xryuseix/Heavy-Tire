use pyo3::prelude::*;
use pyo3::types::PyList;
use std::env;


fn main() -> PyResult<()> {
    let gil = Python::acquire_gil();
    let py = gil.python();

    let syspath: &PyList = py.import("sys")
        .unwrap()
        .get("path")
        .unwrap()
        .try_into()
        .unwrap();

    let path = env::current_dir()?;

    // error[E0277]: the trait bound `std::path::Display<'_>: pyo3::conversion::ToPyObject` is not satisfied
    // syspath.insert(0, path.display()).unwrap();
    syspath.insert(0, format!("{}", path.display())).unwrap();
    
    let hello = py.import("hello")?;
    let response: String = hello.call1("say", ("from Python", ))?.extract()?;
    println!("{}", response);

    Ok(())
}