function extract_property(prop) {
    return function (e) {
        return e[prop]
    }
}

function populate_select(selector, list) {
    var element = $(selector);
    element.html("<option disabled selected> -- Please select -- </option>");  // clear the select
    list.forEach(function (item) {
        element.append(
            $('<option>', {value: item}).text(item)
        );
    })
}

function get_counts(t, attr, vals){
    var t_vals = t.map(extract_property(attr));
    var counts = t_vals.reduce(function (acc, curr) {
        acc[curr] ? acc[curr]++ : acc[curr] = 1;
        return acc;
    }, {});
    return vals.map(function (e) {
        return counts[e] ? parseFloat((100 * counts[e]/t_vals.length).toFixed(2)) : 0.00;
    });
}

function populate_hc_bar(hcObj, attrs, attr, vals){
    var passing = attrs.filter(function (e) {
        return e["FID_STATUS"] == 'Pass'
    });

    var failing = attrs.filter(function (e) {
        return e['FID_STATUS'] != 'Pass'
    });

    var pass_counts = get_counts(passing, attr, vals);
    var fail_counts = get_counts(failing, attr, vals);

    $(hcObj).highcharts({
        chart: {type: 'bar'},
        title: {text: attr + " Value Percentages"},
        subtitle: {text: ''},
        xAxis: {
            categories: vals,
            title: {text: null}
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Percent',
                align: 'high'
            },
            labels: {overflow: 'justify'}
        },
        tooltip: {valueSuffix: ' %'},
        plotOptions: {
            bar: {
                dataLabels: {enabled: true}
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 80,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },
        credits: {enabled: false},
        series:[{
            name: 'Pass',
            data: pass_counts
        },{
            name: 'Fail',
            data: fail_counts
        }]
    });
}

function get_options(list) {
    var index, item, _i, _len, _results;
    _results = [];
    for (index = _i = 0, _len = list.length; _i < _len; index = ++_i) {
        item = list[index];
        _results.push({
            idx: index,
            value: item
        });
    }
    return _results;
}
