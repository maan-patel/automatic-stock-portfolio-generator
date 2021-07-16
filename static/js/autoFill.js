var YAHOO = {
    Finance: {
        SymbolSuggest: {}
    }
};
    
    $("#id_stock_name").autocomplete({
        autoFocus: true,
source: function (request, response) {
$.ajax({
    type: "GET",
    dataType: "jsonp",
    jsonp: "callback",
    jsonpCallback: "YAHOO.Finance.SymbolSuggest.ssCallback",
    data: {
        query: request.term,
        region: 1,
        lang: "en"
        
    },
    cache: true,
    url: "https://autoc.finance.yahoo.com/autoc"
});

YAHOO.Finance.SymbolSuggest.ssCallback = function (data) {
    response($.map(data.ResultSet.Result, function (item) {
        return {
            label: item.name,
            value: item.symbol
        }
    }));
}
},
minLength: 1,
select: function (event, ui) {
    $("#id_stock_name").val(ui.item.name);
},
open: function () {
    $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
},
close: function () {
    $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
}
});