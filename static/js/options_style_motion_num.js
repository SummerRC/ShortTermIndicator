class MotionStrengthLineChart {
    constructor(chart_title, timestamps, zhqds) {
        this.chart_title = chart_title
        this.x_data = timestamps
        this.y_data = zhqds
        this.line_85 =
            {
                type: 'value',
                min: 0,
                max: 85,
                interval: 85,
                splitLine:{
                    show: true,
                    lineStyle: {
                        color: 'white', // 分隔线颜色。
                        width: 1
                    }
                },
                //不显示标签
                axisLabel: {
                    show: false,
                },
            }
        // 指定图表的配置项和数据
        this.option = {
            title: {
                text: this.chart_title ,
                left: 'center',
                top: 30,
            },
            tooltip: {
                trigger: 'axis',
                formatter: '日期: {b} <br/>情绪: {c}',       //鼠标放在该点，显示日期和情绪
                axisPointer: {
                    type: 'line',       //自动吸附到最近的点
                    axis: 'x',
                }
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
            yAxis: [{
                type: 'value',
                min: 0,
                max: 85,
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
                    color: 'black',
                    formatter: function (value, index) {
                        if (value === 85) {
                            return ''
                        } else {
                            return value
                        }
                    },
                },
                axisPointer: {
                    show:true
                }
            }, this.line_85],
            //设觉映射组件，<=35显示绿色，>=65显示红色
            visualMap: [{
                dimension: 1,
                show: false,
                pieces: [{
                    lte: 25,
                    color: 'green'
                },
                {
                    gte: 65,
                    color: 'red'
                }],
                outOfRange: {
                    color: '#5470c6'
                },
            }],
            series: [{
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
            }],
        };
    }
}


