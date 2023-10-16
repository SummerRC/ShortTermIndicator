class MotionStrengthLineChart {
    constructor(chart_title, timestamps, zhqds) {
        this.chart_title = chart_title
        this.x_data = timestamps
        this.y_data = zhqds
        // 指定图表的配置项和数据
        this.option = {
            title: {
                text: this.chart_title ,
                left: 'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: '日期: {b} <br/>情绪: {c}'       //鼠标放在该点，显示日期和情绪
            },
            xAxis: {
                data: this.x_data,
                // 刻度表现会居中
                axisTick: {
                    alignWithLabel: true
                },
                axisLabel: {
                    interval: 'auto',      //0强制显示所有标签
                    //rotate: 90,         //旋转之后能都显示得下，但有点丑
                },
            },
            yAxis: {
                type: 'value',
                min: 0,
                max: 75,
                // 强制间隔是25
                interval: 25,
                // 显示次分割线
                minorSplitLine: {
                    show: true,
                },
                // 次刻度线分割的数量
                minorTick: {
                    splitNumber: 2
                },
                //设置标签样式
                axisLabel: {
                    fontWeight: 'normal',   //bold
                    fontSize: 16,
                    color: 'black'
                }
            },
            // //缩放相关，未完成
            // dataZoom: [
            //     {
            //         show: true,
            //         type: 'inside',
            //         filterMode: 'none',
            //         yAxisIndex: [0],
            //         startValue: 0,
            //         endValue: 100
            //     }
            // ],
            series: [
                {
                    data: this.y_data,
                    type: 'line',

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


