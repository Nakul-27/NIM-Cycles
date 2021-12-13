// This is an implementation of the Basic NIM
// The User enters in n, a, b
// OR randomly pick the Subtraction Set
// use std::env;
use std::cmp;
#[derive(Copy, Clone)]
enum PositionStatus {
    Win,
    Loss,
}

fn main() {
    // let args: Vec<String> = env::args().collect();

    let a = 2;
    let b = 3;
    let c = 5;

    let max = cmp::max(a,cmp::max(b,c));
    let starting_index = max - 1;

    let mut final_array: [u8; 100] = [0; 100];
    let mut position_array: [PositionStatus; 100] = [PositionStatus::Loss; 100];

    for index in starting_index+1..final_array.len() {
	final_array[index] = (final_array[index - a] * final_array[index - b] * final_array[index - c] + 1) % 2;
	if final_array[index] == 1 {
	    position_array[index] = PositionStatus::Win;
	}
    }

    // let mut pos_array: [PositionStatus; 10] = [PositionStatus::Win; 10];
    // let status: PositionStatus = PositionStatus::Win;
    // let another_status: PositionStatus = PositionStatus::Loss;
    // pos_array[0] = status;
    // pos_array[1] = another_status;
    for stat in position_array {
	match stat {
	    PositionStatus::Win => println!("Win"),
	    PositionStatus::Loss => println!("Loss"),
	}
    }

    // assert!(args.len() == 4, "Need 3 arguments: n, a, b.");
    // println!("{:?}, {:?}, {:?}", args[1], args[2], args[3]);
    // println!("{:?}", args);
}
