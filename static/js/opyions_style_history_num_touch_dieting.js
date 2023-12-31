// 历史封板率的折线图表
class OptionsHistoryNumTouchDT {
    constructor(chart_title, trade_day, highest) {
        this.chart_title = chart_title
        this.x_data = trade_day
        this.y_data = highest
        // 指定图表的配置项和数据
        this.option = {
            title: {
                text: this.chart_title ,
                left: 'center',
                top: 10,
            },
            tooltip: {
                trigger: 'axis',
                formatter: '日期: {b} <br/>高度: {c}',       //鼠标放在该点，显示日期和情绪
                axisPointer: {
                    type: 'line',       //自动吸附到最近的点
                    axis: 'x',
                }
            },
            xAxis: {
                data: this.x_data,
                // 刻度表现会居中
                axisTick: {
                    alignWithLabel: true,
                    show: false
                },
                axisLabel: {
                    interval: 'auto',      //0强制显示所有标签
                    rotate: 90,         //旋转之后能都显示得下，但有点丑
                },
                //坐标轴轴线
                axisLine: {
                    show: false,           // 不显示坐标轴线
                },
            },
            yAxis: {
                type: 'value',
                min: 0,
                max: 80,
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
            ],
            //设觉映射组件，<=35显示绿色，>=65显示红色
            visualMap: [{
                dimension: 1,
                show: false,
                pieces: [{
                    lte: 1,
                    color: 'red'
                },
                {
                    gt: 30,
                    color: 'green'
                }],
                outOfRange: {
                    color: '#5470c6'
                },
            }],
        };
    }
}


