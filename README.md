
COMMANDS:
 locust -f wooloadtest.py --no-web  --clients=10 --hatch-rate=5 --only-summary [--host="http://wootest.rtcamp.net/"]


 TOOLS USED:
  1. https://github.com/locustio/locust
  2. https://github.com/cobrateam/splinter

  PREREQUISITE on Site:
  1. Woocommerce Plugin (with dummy data)
  2. WooCommerce Checkout Manager (disable all form options at checkout page)
      - https://wordpress.org/plugins/woocommerce-checkout-manager/
