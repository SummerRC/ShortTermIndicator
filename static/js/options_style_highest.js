// 连板高度的折线图表
class FbRateLineChart {
    constructor(chart_title, trade_day, highest) {
        this.chart_title = chart_title
        this.x_data = trade_day
        this.y_data = highest
        // 指定图表的配置项和数据
        this.option = {
            title: {
                text: this.chart_title,
                left: 'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: '日期: {b} <br/>封板率: {c}'       //鼠标放在该点，显示日期和封板率
            },
            xAxis: {
                data: this.x_data,
                // 刻度表现会居中
                axisTick: {
                    alignWithLabel: true
                },
                axisLabel: {
                    interval: 'auto',      //0强制显示所有标签
                    rotate: 90,            //旋转之后能都显示得下，但有点丑
                },
            },
            yAxis: {
                type: 'value',
                min: 50,
                max: 90,
                // 强制间隔是1
                interval: 10,
                // 显示次分割线
                minorSplitLine: {
                    show: false,
                },
                //设置标签样式
                axisLabel: {
                    fontWeight: 'normal',   //bold
                    fontSize: 16,
                    color: 'black'
                }
            },
            series: [
                {
                    data: this.y_data,
                    type: 'line',
                    smooth: true,

                    label: {
                        // true会显示情绪强度值
                        show: false,
                        position: 'top',
                        textStyle: {
                            fontSize: 8
                        }
                    },
                    colorBy: "series",
                }
            ]
        };
    }
}


