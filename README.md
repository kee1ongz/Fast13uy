## Taobao Auto Purchase Tool - "Fast13uy"

CN:淘宝自动秒杀的简单实现

### Description

"Fast13uy" is an automated login and order placement tool for Taobao, developed using Selenium. This tool provides a convenient and efficient way to automate the process of logging in to Taobao and placing orders. 

### Features

- Automated login to Taobao using Selenium and simulated QR code scanning.
- Quick order placement on Taobao using predefined settings.
- Works reliably within a timeframe of approximately 1 to 2 seconds.
- Suitable for general use and ideal for scenarios such as flash sales and limited-time promotions.
- **Note: "Fast13uy" is not recommended for high-traffic flash sales or situations with a large number of buyers competing for limited stock.**

### Benefits

- Saves time and effort by automating the login and order placement process on Taobao.
- Provides a seamless and efficient experience for users who want to quickly secure their desired products.
- **Offers a reliable method for obtaining Taobao cookies by utilizing Selenium and simulated QR code scanning.**

### Installation

1. Ensure you have Python3 installed on your system.
2. Install the required dependencies by running the following command:

```
pip install selenium
```

3. Download the "Fast13uy" script from the this GitHub repository. You can use `git clone` or download the zip file directly.
4. Make sure the desired purchase time is correct.
5. Run the script and follow the on-screen instructions.

### Usage

1. Launch the "Fast13uy" script.

```
python fast_buy.py
```

1. Enter the desired purchase time in the specified format (e.g., '2023-05-24 10:02:01.000000').
   - It is strongly recommended to advance by about 0.5 to 0.7 seconds
     - e.g. 2023-05-24 10:00:00.000000 ---> 2023-05-24 :09:59:59.500000
2. The script will automatically initiate the login process, simulate QR code scanning, and navigate to the cart page.
3. Once the specified purchase time is reached, the script will attempt to place the order.
4. If successful, the script will display the purchase confirmation and provide the order details.

### Limitations

- Due to the nature of the script and the reliance on Selenium for browser automation, the execution time may vary slightly, typically ranging from 1 to 2 seconds.
- The script is not optimized for scenarios with a high number of concurrent buyers during flash sales or limited-time promotions.

### Acknowledgements

- This script is developed using the Selenium framework.

- Special thanks to the open-source community for their contributions and support.

  ```
  https://zhuanlan.zhihu.com/p/609637690
  ```

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

### Disclaimer

- The "Fast13uy" tool is provided as-is, without any warranty or guarantee of its functionality or effectiveness.
- Use this tool responsibly and in compliance with the terms and conditions of the Taobao platform.
- The developers of this tool are not responsible for any misuse, damages, or legal implications arising from its usage.
