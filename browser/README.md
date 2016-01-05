
COMMANDS:

 `locust -f wooloadtest.py --no-web  --clients=10 --hatch-rate=5 --only-summary --host="http://wootest.rtcamp.net/"`


 TOOLS USED:
  - https://github.com/locustio/locust
  - https://github.com/cobrateam/splinter

<br>
 PREREQUISITE on Site:
  - Woocommerce Plugin (with dummy data)
  - WooCommerce Checkout Manager (disable all form options at checkout page)
      - https://wordpress.org/plugins/woocommerce-checkout-manager/
