// 冰点、沸点样式
class FreezingBoilingPointStyleOptions {
    constructor(chart_title, timestamps, zhqds) {
        this.chart_title = chart_title
        this.x_data = timestamps
        this.y_data = zhqds
        this.wipe = new WipeFreezingBoilingPoint()

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
                    show: false,
                    alignWithLabel: true
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
            yAxis: [
                {
                type: 'value',
                min: 0,
                max: 65,
                // 强制间隔是5
                interval: 5,
                //分割线样式
                splitLine:{
                    show: true,
                    lineStyle: {
                        color: '#495B71', // 分隔线颜色。
                        width: 2
                    }
                },
                //设置标签样式
                axisLabel: {
                    margin: 16,
                    show: true,
                    formatter: function (value, index) {
                        var texts = value
                        if (index === 1) {
                            texts = '{a|冰点}'
                        } else if(index === 3) {
                            texts = '{b|过冷}'
                        } else if(index === 5) {
                            texts = '{c|微冷}'
                        } else if(index === 7) {
                            texts = '{d|微热}'
                        } else if(index === 9) {
                            texts = '{e|过热}'
                        } else if(index === 11) {
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
                // 擦线：10、20、30、40、50、60、65  ｜  15、30、45、60     |  剩：5（目标）、25、35、55
                this.wipe.line_wipe_10, this.wipe.line_wipe_15,
                // 画线：15（目标）、30、45、60、65    ｜   剩：5（目标）、15（目标）、25、30、35、45、55、60、65
                this.wipe.line_draw_15,
                //擦线：25、50、65   ｜   35、65      |   剩：5（目标）、15（目标）、30、45、55、60
                this.wipe.line_wipe_25, this.wipe.line_wipe_35,
                //擦线：45、65  ｜   30、60、65       ｜     剩：5（目标）、15（目标）、55
                this.wipe.line_wipe_45, this.wipe.line_wipe_30,
                //画线：55、65                       ｜     剩：5（目标）、15（目标）、55（目标）、65
                this.wipe.line_draw_55,
                //画线：45、65                       ｜     剩：5（目标）、15（目标）、55（目标）、45（目标）、65
                this.wipe.line_draw_45,
                //画线：30、60、65                   ｜     剩：5（目标）、15（目标）、30（目标）、45（目标）、55（目标）、60、65
                this.wipe.line_draw_30,
                //擦线：0、60、65                    ｜     剩：5（目标）、15（目标）、30（目标）、45（目标）、55（目标）
                this.wipe.line_wipe_60_65
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
                    lte: 5,
                    color: 'green'
                },
                {
                    gt: 45,
                    color: 'red'
                }],
                outOfRange: {
                    color: '#5470c6'
                },
            }],
        };
    }
}


