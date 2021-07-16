let stock_name = document.getElementById('stock').innerHTML;
  let graph_type = document.getElementById('chart_type').innerHTML;
  // console.log(stock_name)
  new TradingView.widget(
  {
  "width": 980,
  "height": 610,
  "symbol": stock_name,
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "light",
  "style": graph_type,
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_b0d5f"
}
  );