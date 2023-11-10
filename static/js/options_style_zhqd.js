class MotionZhqdLineChart {
    constructor(chart_title, timestamps, zhqds) {
        this.chart_title = chart_title
        this.x_data = timestamps
        this.y_data = zhqds
        this.wipe = new WipeZhqd()

        // 指定图表的配置项和数据
        this.option = {
            title: {
                text: this.chart_title ,
                left: 'center',
                top: 50,
            },
            tooltip: {
                trigger: 'axis',
                formatter: function(params) {
                    let value = `${params[0].value}`
                    value = parseInt(value) + 20
                    return  '日期: ' + `${params[0].name}` + '<br/>' + '情绪: ' + value
                },
                axisPointer: {
                    type: 'line',       //自动吸附到最近的点
                    axis: 'x',
                }
            },
            xAxis: {
                data: this.x_data,
                // 刻度表现会居中
                axisTick: {
                    show: false,            //不显示坐标轴刻度
                    alignWithLabel: true
                },
                axisLabel: {
                    interval: 'auto',      //0强制显示所有标签
                    rotate: 90,          //旋转之后能都显示得下，但有点丑
                },
                axisLine: {
                    show: false,           // 不显示坐标轴线
                },
            },
            yAxis: [{
                type: 'value',
                min: 0,
                max: 65,
                // 强制间隔是25
                interval: 5,
                // 显示次分割线
                minorSplitLine: {
                    show: false,
                },
                //设置标签样式
                axisLabel: {
                    fontWeight: 'normal',   //bold
                    fontSize: 16,
                    color: 'black',
                    formatter: function (value, index) {
                        if (value === 55 || value === 30 || value === 5 ) {
                            return value + 20
                        } else {
                            return ''
                        }
                    },
                },
                //不显示指示器
                axisPointer: {
                    show:false
                }
            }, this.wipe.line_wipe_10, this.wipe.line_wipe_15, this.wipe.line_wipe_25, this.wipe.line_wipe_35,
            this.wipe.line_wipe_45, this.wipe.line_draw_30, this.wipe.line_wipe_60_65],
            //设觉映射组件，<=35显示绿色，>=65显示红色
            visualMap: [{
                dimension: 1,
                show: false,
                pieces: [{
                    lte: 5,
                    color: 'green'
                },
                {
                    gte: 45,
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


