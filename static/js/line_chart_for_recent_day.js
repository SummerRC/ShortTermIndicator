class MotionStrengthRecentDay {
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
                interval: 5,
                //设置标签样式
                axisLabel: {
                    margin: 16,
                    show: true,
                    formatter: function (value, index) {
                        var texts = value
                        if (index === 5) {
                            texts = '{a|冰点}'
                        } else if(index === 7) {
                            texts = '{b|过冷}'
                        } else if(index === 9) {
                            texts = '{c|微冷}'
                        } else if(index === 11) {
                            texts = '{d|微热}'
                        } else if(index === 13) {
                            texts = '{e|过热}'
                        } else if(index === 15) {
                            texts = '{f|沸点}'
                        } else {
                            texts = ''
                        }
                        return texts
                    },
                    rich: {
                        a: {
                            color: 'black',
                            lineHeight: 16,
                            borderWidth: 2,
                            borderColor: 'black',
                            borderType: 'solid',
                            borderRadius: 4,
                            width: 52,
                            height:20,
                            align: 'center'
                        },
                        b: {
                            color: 'black',
                            lineHeight: 16,
                            borderWidth: 2,
                            borderColor: '#7487BF',
                            borderType: 'solid',
                            borderRadius: 4,
                            width: 52,
                            height:20,
                            align: 'center'
                        },
                        c: {
                            color: 'black',
                            lineHeight: 16,
                            borderWidth: 2,
                            borderColor: '#9EAEBD',
                            borderType: 'solid',
                            borderRadius: 4,
                            width: 52,
                            height:20,
                            align: 'center'
                        },
                        d: {
                            color: 'black',
                            lineHeight: 16,
                            borderWidth: 2,
                            borderColor: '#DF97A1',
                            borderType: 'solid',
                            borderRadius: 4,
                            width: 52,
                            height:20,
                            align: 'center'
                        },
                        e: {
                            color: 'black',
                            lineHeight: 16,
                            borderWidth: 2,
                            borderColor: '#D15B64',
                            borderType: 'solid',
                            borderRadius: 4,
                            width: 52,
                            height:20,
                            align: 'center'
                        },
                        f: {
                            color: 'black',
                            lineHeight: 16,
                            borderWidth: 2,
                            borderColor: 'red',
                            borderType: 'solid',
                            borderRadius: 4,
                            width: 52,
                            height:20,
                            align: 'center'
                        }
                    }
                },
            },

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


