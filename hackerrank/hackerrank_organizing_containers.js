function organizingContainers(container) {
    let possible = "Possible";
    let impossible = "Impossible";
    let sum_of_each_row = container.map(r => r.reduce((a,b) => a+b));
    let sum_of_each_column = container.reduce((a,b) => a.map((x, i) => x + b[i]));

    sum_of_each_row.sort();
    sum_of_each_column.sort();
    console.log(sum_of_each_row);
    console.log(sum_of_each_column);
    
    if (JSON.stringify(sum_of_each_row)==JSON.stringify(sum_of_each_column)) {
        return possible;
    }
    else {
        return impossible;
    }
}