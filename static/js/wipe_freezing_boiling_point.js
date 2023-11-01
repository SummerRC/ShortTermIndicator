 // 采用覆盖法+多Y轴的方法，定义不同样式的分割线
class WipeFreezingBoilingPoint {
      constructor() {
        this.line_draw_55 =
            {
                type: 'value',
                min: 0,
                max: 65,
                interval: 55,
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
        this.line_draw_45 =
            {
                type: 'value',
                min: 0,
                max: 65,
                interval: 45,
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
        this.line_wipe_30 =
            {
                type: 'value',
                min: 0,
                max: 65,
                interval: 30,
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
        this.line_draw_30 =
            {
                type: 'value',
                min: 0,
                max: 65,
                interval: 30,
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
        this.line_draw_15 =
            {
                type: 'value',
                min: 0,
                max: 65,
                interval: 15,
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
          //擦除60、65七条分割线
          this.line_wipe_60_65 =
              {
                  type: 'value',
                  min: 0,
                  max: 65,
                  interval: 60,
                  splitLine: {
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
          //擦除10、20、30、40、50、60、65七条分割线
          this.line_wipe_10 =
              {
                  type: 'value',
                  min: 0,
                  max: 65,
                  interval: 10,
                  splitLine: {
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
          //擦除15、30、45、60、65五条分割线
          this.line_wipe_15 =
              {
                  type: 'value',
                  min: 0,
                  max: 65,
                  interval: 15,
                  splitLine: {
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
          //擦除25、50、65三条分割线
          this.line_wipe_25 =
              {
                  type: 'value',
                  min: 0,
                  max: 65,
                  interval: 25,
                  splitLine: {
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
          //擦除35、65四条分割线
          this.line_wipe_35 =
              {
                  type: 'value',
                  min: 0,
                  max: 65,
                  interval: 35,
                  splitLine: {
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
          //擦除45、65四条分割线
          this.line_wipe_45 =
              {
                  type: 'value',
                  min: 0,
                  max: 65,
                  interval: 45,
                  splitLine: {
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

      }
}