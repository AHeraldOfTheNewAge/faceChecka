use std::env;
use std::path::Path;

fn is_image(img:&str) -> bool{
    let file_is = Path::new(img).is_file();

    if !file_is {
        return false;
    }

    return true;
}

fn main() {
    let mut images: Vec<_> = env::args().collect();
    images.remove(0);//remove the call to this file..

    for image in images{
        println!("imagine? {}", is_image(image.as_str()));
    }

    //println!("--------------");
    //println!("{:?}", images);
    // println!();
    //println!("facem debug ----- {:?}", is_image("taggus"));
}
