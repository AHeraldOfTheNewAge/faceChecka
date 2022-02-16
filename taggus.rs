use std::env;
use std::path::Path;

/**
    Loosely check if file is an image
*/
fn is_image(img:String) -> bool{
    let approved_file_types = vec!["png", "jpg", "jpeg"];
    let mut is_approved_file_type = false;

    for file_type in approved_file_types {
        if img.ends_with(file_type) {
            is_approved_file_type = true;
            break;
        }
    }

    if !is_approved_file_type {
        return false;
    }

    let file_exists = Path::new(img.as_str()).is_file();

    if !file_exists {
        return false;
    }

    return true;
}

fn main() {
    let mut images: Vec<String> = env::args().collect();
    images.remove(0);//remove the call to this file..

    for image in images{
        println!("imagine? {}", is_image(image));
    }

    //println!("--------------");
    //println!("{:?}", images);
    // println!();
    //println!("facem debug ----- {:?}", is_image("taggus"));
}
