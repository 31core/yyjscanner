# Yunyuejuan account scanner
## Usage
This script will test all the Yunyuejuan accounts from 000 to 999 to find out the accessible ones.

## Install
```shell
pip3 install requests
```

## API
POST this data to `http://sc.yunyuejuan.net/SystemLogin` to check if the account is accessible.
```javascript
{
	"j_username": "username",
	"j_password": "123456" //Default password
}
```
Thanks to @pumkin1001 for providing the API.

