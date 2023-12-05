use std::fs::File;
use std::io::prelude::*;


#[derive(Debug, Clone)]
struct Animal {
    name: String,
    price: i32,
    space: i32,
}


fn read_file() -> (Vec<Animal>, i32) {
    let mut file = File::open("/home/stranavadavid/RustroverProjects/zoo/src/animals.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();


    let split_content: Vec<&str> = contents.split("\n").collect();

    let mut animals: Vec<&str> = Vec::new();
    let mut prices: Vec<i32> = Vec::new();
    let mut spaces: Vec<i32> = Vec::new();
    let mut max_size: i32 = 0;

    for (index, line) in split_content.into_iter().enumerate() {
        // Animals line
        if index == 0 {
            animals = line.split(" ").collect();
            continue;
        }


        // Spaces
        if index == 1 {
            let split_line: Vec<&str> = line.split(" ").collect();

            for item in split_line {
                spaces.push(item.parse::<i32>().unwrap());
            }
        }

        // Prices
        if index == 2 {
            let split_line: Vec<&str> = line.split(" ").collect();

            for item in split_line {
                prices.push(item.parse::<i32>().unwrap());
            }
        }

        // Max size
        if index == 3 {
            max_size = line.parse::<i32>().unwrap();
        }

    }

    if animals.len() != spaces.len() && spaces.len() != prices.len() {
        // lengths of arrays dont match
        return (Vec::new(), 0);
    }

    let mut result_animals: Vec<Animal> = Vec::new();

    for (index, animal) in animals.iter().enumerate(){
        let new_animal = Animal {
            name: animal.to_string(),
            price: prices.get(index).unwrap().to_owned(),
            space: spaces.get(index).unwrap().to_owned(),
        };
        result_animals.push(new_animal);
    }

    return (result_animals, max_size);
}

fn do_some_recursion(animals: &Vec<Animal>, max_size: i32, n: usize, selected_animals: Vec<Animal>) -> (i32, Vec<Animal>) {
    if n == 0 || max_size == 0 {
        return (0, selected_animals)
    }

    let current_animal = animals.get(n - 1).unwrap().to_owned();

    if current_animal.space > max_size {
        return do_some_recursion(&animals, max_size, n - 1, selected_animals)
    }

    let mut new_animals_with = selected_animals.to_owned();
    new_animals_with.push(current_animal.clone());

    let (price_with, animals_with) = do_some_recursion(&animals, max_size - &current_animal.space, n - 1, new_animals_with);
    let (price_without, animals_without) = do_some_recursion(animals, max_size, n - 1, selected_animals);

    if price_with + &current_animal.price > price_without {
        return (price_with + &current_animal.price, animals_with)
    }

    return (price_without, animals_without);

    return (0, Vec::new())
}


fn main() {
    let (animals, max_size) = read_file();
    let results = do_some_recursion(&animals, max_size, animals.len(), Vec::new());
    println!("{:?}", results);
}
