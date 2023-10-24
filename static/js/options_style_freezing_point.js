// 冰点、沸点样式
class FreezingPointStyleOptions {
    constructor(chart_title, timestamps, zhqds) {
        this.chart_title = chart_title
        this.x_data = timestamps
        this.y_data = zhqds
        // 采用覆盖法+多Y轴的方法，定义不同样式的分割线
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
                        width: 2
                    }
                },
                //不显示标签
                axisLabel: {
                    show: false,
                },
            }
        this.line_75 =
            {
                type: 'value',
                min: 0,
                max: 85,
                interval: 75,
                splitLine:{
                    show: true,
                    lineStyle: {
                        color: '#ad2521', // 分隔线颜色。
                        width: 2
                    }
                },
                //不显示标签
                axisLabel: {
                    show: false,
                },
            }
        this.line_70 =
            {
                type: 'value',
                min: 0,
                max: 85,
                interval: 70,
                splitLine:{
                    show: true,
                    lineStyle: {
                        color: 'white', // 分隔线颜色。
                        width: 2
                    }
                },
                //不显示标签
                axisLabel: {
                    show: false,
                },
            }
        this.line_65 =
            {
                type: 'value',
                min: 0,
                max: 85,
                interval: 65,
                splitLine:{
                    show: true,
                    lineStyle: {
                        color: 'pink', // 分隔线颜色。
                        width: 2,
                       type: 'dashed'
                    }
                },
                //不显示标签
                axisLabel: {
                    show: false,
                }
            }
        this.line_50 =
            {
                type: 'value',
                min: 0,
                max: 85,
                interval: 50,
                splitLine:{
                    show: true,
                    lineStyle: {
                       color: 'white', // 分隔线颜色。
                        width: 2,
                    }
                },
                //不显示标签
                axisLabel: {
                    show: false,
                }
            }
        this.line_50_twice =
            {
                type: 'value',
                min: 0,
                max: 85,
                interval: 50,
                splitLine:{
                    show: true,
                    lineStyle: {
                       color: '#E0E6F1', // 分隔线颜色。
                       type: 'dashed',
                        width: 2
                    }
                },
                //不显示标签
                axisLabel: {
                    show: false,
                }
            }
        this.line_35 =
            {
                type: 'value',
                min: 0,
                max: 85,
                interval: 35,
                splitLine:{
                    show: true,
                    lineStyle: {
                        color: '#457B6D', // 分隔线颜色。
                        width: 2,
                        type: 'dashed'
                    }
                },
                //不显示标签
                axisLabel: {
                    show: false,
                }
            }
        this.line_25 =
            {
                type: 'value',
                min: 0,
                max: 85,
                interval: 25,
                splitLine:{
                    show: true,
                    lineStyle: {
                       color: '#495B71', // 分隔线颜色。
                        width: 2
                    }
                },
                //不显示标签
                axisLabel: {
                    show: false,
                }
            }
        // 指定图表的配置项和数据
        this.option = {
            title: {
                text: this.chart_title ,
                left: 'center',
                top: 30,

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
                //坐标轴轴线
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: 'black',
                    }
                }
            },
            yAxis: [
                {
                type: 'value',
                min: 0,
                max: 85,
                // 强制间隔是25
                interval: 5,
                //分割线样式
                splitLine:{
                    show: false,
                    lineStyle: {
     	                color: ['#ccc'], // 分隔线颜色。
     	                width: 1, // 分隔线线宽
     	                type: 'dashed', // 线的类型
     	                opacity: 1 // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。
                    }
                },
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
            }, this.line_25, this.line_35, this.line_50, this.line_50_twice, this.line_65, this.line_70, this.line_75,
                this.line_85
            ],

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
                },
            ],
            //设觉映射组件，<=35显示绿色，>=65显示红色
            visualMap: [{
                dimension: 1,
                show: false,
                pieces: [{
                    lte: 25,
                    color: 'green'
                },
                {
                    gt: 65,
                    color: 'red'
                }],
                outOfRange: {
                    color: '#5470c6'
                },
            }],
        };
    }
}


