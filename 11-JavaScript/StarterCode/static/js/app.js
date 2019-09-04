// from data.js
var tableData = data;
var tbody = d3.select("tbody");

// make function to create table of data
function tableDisplay(data) {
    
    data.forEach((response) => {
    var row = tbody.append('tr');
    Object.entries(response).forEach(([key, value]) => {

    var cell = row.append('td');
    cell.text(value);
    });
})};

tableDisplay(tableData);

// create function that returns info for specific date entered
var filterButton = d3.select('#filter-btn');
var inputElement = d3.select('#datetime');
var inputValue = inputElement.property("value");

function handleClick() {
    // prevent page from refreshing
    d3.event.preventDefault()

    // create new variable that equals the filtered data
    let filterData = tableData.filter(response => response.datetime);

    // create conditional that displays table if user's input equals the datetime in filterData
    if (filterData === inputValue) {

        tableDisplay(filterData);
    };
    
    
};

filterButton.on('click', handleClick)
