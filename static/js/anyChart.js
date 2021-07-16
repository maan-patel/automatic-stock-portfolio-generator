anychart.onDocumentLoad(function () {
    // create an instance of a pie chart
    var chart = anychart.pie();
    // set the data
    lis = document.querySelectorAll('li')
    chart.data([
      [lis[0].textContent, 5],
      [lis[1].textContent, 2],
      [lis[2].textContent, 2],
      [lis[3].textContent, 2],
      [lis[4].textContent, 1]
    ]);
    // set chart title
  
    // set the container element
    chart.container("container");
    // initiate chart display
    chart.draw();
  });