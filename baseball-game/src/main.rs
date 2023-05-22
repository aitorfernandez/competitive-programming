fn cal_points(operations: Vec<String>) -> i32 {
    let mut points: Vec<i32> = Vec::new();

    for o in operations {
        match o.as_ref() {
            "C" => {
                let _ = points.pop();
            }
            "D" => points.push(points[points.len() - 1] * 2),
            "+" => points.push(points[points.len() - 1] + points[points.len() - 2]),
            _ => points.push(o.parse::<i32>().unwrap()),
        }
    }

    points.iter().sum()
}

fn main() {
    assert_eq!(
        cal_points(vec![
            "5".to_string(),
            "2".to_string(),
            "C".to_string(),
            "D".to_string(),
            "+".to_string()
        ]),
        30
    );
}
