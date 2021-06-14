var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var xhr = new XMLHttpRequest();

function httpGet(url)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
let search_query = document.getElementById('#id_stock_name')
// const search_query = "GOO"
const url = `http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=${search_query}&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback`

let text = httpGet(url)
var j = text.slice(39,-2)
let data = JSON.parse(j)["ResultSet"]["Result"]


function stock_drop_down(data){
  let arr_drop = []
  for (let i = 0; i < data.length; i ++) {
    let sym = data[i]["symbol"]
    let nam = data[i]["name"]
    arr_drop.push(`${sym.toUpperCase()} - ${nam}`)
  }
  return arr_drop
}
var a = stock_drop_down(data)