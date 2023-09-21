use std::fs::File;
use std::io::prelude::*;
use std::time::Instant;

fn parse_file_line_into_line(line: &str) -> Vec<i16> {
    let mut new_line: Vec<i16> = Vec::new();
    let split_line: Vec<&str> = line.split(" ").collect();

    for item in split_line {
        new_line.push(item.parse::<i16>().unwrap());
    }

    return new_line;
}

fn read_file(key: &str) -> (Vec<Vec<i16>>, Vec<Vec<i16>>) {
    let mut file = File::open(key).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();


    let split_content: Vec<&str> = contents.split("\r\n").collect();

    let mut size = 0;
    let mut matrix_first: Vec<Vec<i16>> = Vec::new();
    let mut matrix_second: Vec<Vec<i16>> = Vec::new();

    for (index, line) in split_content.into_iter().enumerate() {
        if index == 0 {
            size = line.parse::<i16>().unwrap();
            continue;
        }

        if matrix_first.len() < size as usize {
            matrix_first.push(parse_file_line_into_line(line));
        } else {
            matrix_second.push(parse_file_line_into_line(line));
        }

    }

    (matrix_first, matrix_second)
}


fn sum(matrix_first: &Vec<Vec<i16>>, matrix_second: &Vec<Vec<i16>>) -> Vec<Vec<i16>>{
    let mut result: Vec<Vec<i16>> = Vec::new();

    for (line_index, line) in matrix_first.into_iter().enumerate() {
        result.push(Vec::new());
        for (item_index, item) in line.into_iter().enumerate() {
            result[line_index].push(item + matrix_second[line_index][item_index]);
        }
    }

    result
}

fn difference(matrix_first: &Vec<Vec<i16>>, matrix_second: &Vec<Vec<i16>>) -> Vec<Vec<i16>>{
    let mut result: Vec<Vec<i16>> = Vec::new();

    for (line_index, line) in matrix_first.into_iter().enumerate() {
        result.push(Vec::new());
        for (item_index, item) in line.into_iter().enumerate() {
            result[line_index].push(item - matrix_second[line_index][item_index]);
        }
    }

    result
}

fn print_matrix(matrix: Vec<Vec<i16>>) {
    for line in matrix {
        let line_as_strings: Vec<String> = line.into_iter().map(|item| format!("{item}")).collect();
        println!("{}", line_as_strings.join(" "))
    }
}

fn main() {
    let now = Instant::now();
    let (matrix_first, matrix_second) = read_file("/home/stranavadavid/RustroverProjects/untitled/src/01.in");

    let sum_result = sum(&matrix_first, &matrix_second);
    let difference_result = difference(&matrix_first, &matrix_second);
    print_matrix(sum_result);
    print_matrix(difference_result);
    println!("Ellapsed: {}", now.elapsed().as_micros());
}