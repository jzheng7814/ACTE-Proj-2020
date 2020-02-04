from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from pickle import load, dump
from os.path import exists
from json import dumps

credentials = None
if exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        credentials = load(token)
if not credentials or not credentials.valid:
    flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', 'https://www.googleapis.com/auth/documents.readonly')
    credentials = flow.run_local_server(port = 0)
    with open('token.pickle', 'wb') as token:
        dump(credentials, token)

service = build('docs', 'v1', credentials=credentials)

doc = service.documents().get(documentId = '1Etz6RSbPxsqGNQ1kp6WQFqKHOZ6_uaqxDv-TD5hVmF0').execute()
"insertTable": {
                    "rows": 4,
                    "columns": 4,
                    "tableRows": [
                        {
                            "startIndex": 129,
                            "endIndex": 280,
                            "tableCells": [
                                {
                                    "startIndex": 130,
                                    "endIndex": 169,
                                    "content": [
                                        {
                                            "startIndex": 131,
                                            "endIndex": 137,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 131,
                                                        "endIndex": 137,
                                                        "textRun": {
                                                            "content": "Word: %s\n" % data[i * 4][0],
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 137,
                                            "endIndex": 138,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 137,
                                                        "endIndex": 138,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 138,
                                            "endIndex": 139,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 138,
                                                        "endIndex": 139,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 139,
                                            "endIndex": 155,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 139,
                                                        "endIndex": 155,
                                                        "textRun": {
                                                            "content": "Part of speech: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 155,
                                            "endIndex": 156,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 155,
                                                        "endIndex": 156,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 156,
                                            "endIndex": 157,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 156,
                                                        "endIndex": 157,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 157,
                                            "endIndex": 169,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 157,
                                                        "endIndex": 169,
                                                        "textRun": {
                                                            "content": "Definition: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderLeft": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderTop": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 169,
                                    "endIndex": 205,
                                    "content": [
                                        {
                                            "startIndex": 170,
                                            "endIndex": 205,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 170,
                                                        "endIndex": 205,
                                                        "textRun": {
                                                            "content": "Use the word in your own sentence.\n %s \n" % ,
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "CENTER",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderRight": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderTop": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 205,
                                    "endIndex": 244,
                                    "content": [
                                        {
                                            "startIndex": 206,
                                            "endIndex": 212,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 206,
                                                        "endIndex": 212,
                                                        "textRun": {
                                                            "content": "Word: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 212,
                                            "endIndex": 213,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 212,
                                                        "endIndex": 213,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 213,
                                            "endIndex": 214,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 213,
                                                        "endIndex": 214,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 214,
                                            "endIndex": 230,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 214,
                                                        "endIndex": 230,
                                                        "textRun": {
                                                            "content": "Part of speech: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 230,
                                            "endIndex": 231,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 230,
                                                        "endIndex": 231,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 231,
                                            "endIndex": 232,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 231,
                                                        "endIndex": 232,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 232,
                                            "endIndex": 244,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 232,
                                                        "endIndex": 244,
                                                        "textRun": {
                                                            "content": "Definition: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderLeft": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderTop": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 244,
                                    "endIndex": 280,
                                    "content": [
                                        {
                                            "startIndex": 245,
                                            "endIndex": 280,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 245,
                                                        "endIndex": 280,
                                                        "textRun": {
                                                            "content": "Use the word in your own sentence.\n %s \n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "CENTER",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderRight": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderTop": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                }
                            ],
                            "tableRowStyle": {
                                "minRowHeight": {
                                    "magnitude": 184.3125,
                                    "unit": "PT"
                                }
                            }
                        },
                        {
                            "startIndex": 280,
                            "endIndex": 466,
                            "tableCells": [
                                {
                                    "startIndex": 281,
                                    "endIndex": 340,
                                    "content": [
                                        {
                                            "startIndex": 282,
                                            "endIndex": 339,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 282,
                                                        "endIndex": 339,
                                                        "textRun": {
                                                            "content": "Draw a picture to help you remember/understand the word.\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 339,
                                            "endIndex": 340,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 339,
                                                        "endIndex": 340,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderLeft": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderBottom": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 340,
                                    "endIndex": 374,
                                    "content": [
                                        {
                                            "startIndex": 341,
                                            "endIndex": 353,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 341,
                                                        "endIndex": 353,
                                                        "textRun": {
                                                            "content": "2 Synonyms: %s, %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 353,
                                            "endIndex": 354,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 353,
                                                        "endIndex": 354,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 354,
                                            "endIndex": 355,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 354,
                                                        "endIndex": 355,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 355,
                                            "endIndex": 356,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 355,
                                                        "endIndex": 356,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 356,
                                            "endIndex": 357,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 356,
                                                        "endIndex": 357,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 357,
                                            "endIndex": 358,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 357,
                                                        "endIndex": 358,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 358,
                                            "endIndex": 359,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 358,
                                                        "endIndex": 359,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 359,
                                            "endIndex": 360,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 359,
                                                        "endIndex": 360,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 360,
                                            "endIndex": 361,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 360,
                                                        "endIndex": 361,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 361,
                                            "endIndex": 373,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 361,
                                                        "endIndex": 373,
                                                        "textRun": {
                                                            "content": "2 Antonyms: %s, %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 373,
                                            "endIndex": 374,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 373,
                                                        "endIndex": 374,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderRight": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderBottom": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 374,
                                    "endIndex": 433,
                                    "content": [
                                        {
                                            "startIndex": 375,
                                            "endIndex": 402,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 375,
                                                        "endIndex": 402,
                                                        "textRun": {
                                                            "content": "Draw a picture to help you\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 402,
                                            "endIndex": 432,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 402,
                                                        "endIndex": 432,
                                                        "textRun": {
                                                            "content": "remember/understand the word.\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 432,
                                            "endIndex": 433,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 432,
                                                        "endIndex": 433,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderLeft": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderBottom": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 433,
                                    "endIndex": 466,
                                    "content": [
                                        {
                                            "startIndex": 434,
                                            "endIndex": 446,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 434,
                                                        "endIndex": 446,
                                                        "textRun": {
                                                            "content": "2 Synonyms: %s, %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 446,
                                            "endIndex": 447,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 446,
                                                        "endIndex": 447,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 447,
                                            "endIndex": 448,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 447,
                                                        "endIndex": 448,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 448,
                                            "endIndex": 449,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 448,
                                                        "endIndex": 449,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 449,
                                            "endIndex": 450,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 449,
                                                        "endIndex": 450,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 450,
                                            "endIndex": 451,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 450,
                                                        "endIndex": 451,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 451,
                                            "endIndex": 452,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 451,
                                                        "endIndex": 452,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 452,
                                            "endIndex": 453,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 452,
                                                        "endIndex": 453,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 453,
                                            "endIndex": 454,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 453,
                                                        "endIndex": 454,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 454,
                                            "endIndex": 466,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 454,
                                                        "endIndex": 466,
                                                        "textRun": {
                                                            "content": "2 Antonyms: %s, %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderRight": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderBottom": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                }
                            ],
                            "tableRowStyle": {
                                "minRowHeight": {
                                    "magnitude": 184.3125,
                                    "unit": "PT"
                                }
                            }
                        },
                        {
                            "startIndex": 466,
                            "endIndex": 617,
                            "tableCells": [
                                {
                                    "startIndex": 467,
                                    "endIndex": 506,
                                    "content": [
                                        {
                                            "startIndex": 468,
                                            "endIndex": 474,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 468,
                                                        "endIndex": 474,
                                                        "textRun": {
                                                            "content": "Word: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 474,
                                            "endIndex": 475,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 474,
                                                        "endIndex": 475,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 475,
                                            "endIndex": 476,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 475,
                                                        "endIndex": 476,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 476,
                                            "endIndex": 492,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 476,
                                                        "endIndex": 492,
                                                        "textRun": {
                                                            "content": "Part of speech: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 492,
                                            "endIndex": 493,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 492,
                                                        "endIndex": 493,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 493,
                                            "endIndex": 494,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 493,
                                                        "endIndex": 494,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 494,
                                            "endIndex": 506,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 494,
                                                        "endIndex": 506,
                                                        "textRun": {
                                                            "content": "Definition: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderLeft": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderTop": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 506,
                                    "endIndex": 542,
                                    "content": [
                                        {
                                            "startIndex": 507,
                                            "endIndex": 542,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 507,
                                                        "endIndex": 542,
                                                        "textRun": {
                                                            "content": "Use the word in your own sentence.\n %s \n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "CENTER",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderRight": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderTop": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 542,
                                    "endIndex": 581,
                                    "content": [
                                        {
                                            "startIndex": 543,
                                            "endIndex": 549,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 543,
                                                        "endIndex": 549,
                                                        "textRun": {
                                                            "content": "Word: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 549,
                                            "endIndex": 550,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 549,
                                                        "endIndex": 550,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 550,
                                            "endIndex": 551,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 550,
                                                        "endIndex": 551,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 551,
                                            "endIndex": 567,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 551,
                                                        "endIndex": 567,
                                                        "textRun": {
                                                            "content": "Part of speech: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 567,
                                            "endIndex": 568,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 567,
                                                        "endIndex": 568,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 568,
                                            "endIndex": 569,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 568,
                                                        "endIndex": 569,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 569,
                                            "endIndex": 581,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 569,
                                                        "endIndex": 581,
                                                        "textRun": {
                                                            "content": "Definition: %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderLeft": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderTop": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 581,
                                    "endIndex": 617,
                                    "content": [
                                        {
                                            "startIndex": 582,
                                            "endIndex": 617,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 582,
                                                        "endIndex": 617,
                                                        "textRun": {
                                                            "content": "Use the word in your own sentence.\n %s \n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "CENTER",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "avoidWidowAndOrphan": false
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderRight": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderTop": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                }
                            ],
                            "tableRowStyle": {
                                "minRowHeight": {
                                    "magnitude": 184.3125,
                                    "unit": "PT"
                                }
                            }
                        },
                        {
                            "startIndex": 617,
                            "endIndex": 802,
                            "tableCells": [
                                {
                                    "startIndex": 618,
                                    "endIndex": 677,
                                    "content": [
                                        {
                                            "startIndex": 619,
                                            "endIndex": 646,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 619,
                                                        "endIndex": 646,
                                                        "textRun": {
                                                            "content": "Draw a picture to help you\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 646,
                                            "endIndex": 676,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 646,
                                                        "endIndex": 676,
                                                        "textRun": {
                                                            "content": "remember/understand the word.\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 676,
                                            "endIndex": 677,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 676,
                                                        "endIndex": 677,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderLeft": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderBottom": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 677,
                                    "endIndex": 711,
                                    "content": [
                                        {
                                            "startIndex": 678,
                                            "endIndex": 690,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 678,
                                                        "endIndex": 690,
                                                        "textRun": {
                                                            "content": "2 Synonyms: %s, %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 690,
                                            "endIndex": 691,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 690,
                                                        "endIndex": 691,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 691,
                                            "endIndex": 692,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 691,
                                                        "endIndex": 692,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 692,
                                            "endIndex": 693,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 692,
                                                        "endIndex": 693,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 693,
                                            "endIndex": 694,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 693,
                                                        "endIndex": 694,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 694,
                                            "endIndex": 695,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 694,
                                                        "endIndex": 695,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 695,
                                            "endIndex": 696,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 695,
                                                        "endIndex": 696,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 696,
                                            "endIndex": 697,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 696,
                                                        "endIndex": 697,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 697,
                                            "endIndex": 698,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 697,
                                                        "endIndex": 698,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 698,
                                            "endIndex": 710,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 698,
                                                        "endIndex": 710,
                                                        "textRun": {
                                                            "content": "2 Antonyms: %s, %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 710,
                                            "endIndex": 711,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 710,
                                                        "endIndex": 711,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderRight": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderBottom": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 711,
                                    "endIndex": 769,
                                    "content": [
                                        {
                                            "startIndex": 712,
                                            "endIndex": 739,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 712,
                                                        "endIndex": 739,
                                                        "textRun": {
                                                            "content": "Draw a picture to help you\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 739,
                                            "endIndex": 769,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 739,
                                                        "endIndex": 769,
                                                        "textRun": {
                                                            "content": "remember/understand the word.\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderLeft": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderBottom": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                },
                                {
                                    "startIndex": 769,
                                    "endIndex": 802,
                                    "content": [
                                        {
                                            "startIndex": 770,
                                            "endIndex": 782,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 770,
                                                        "endIndex": 782,
                                                        "textRun": {
                                                            "content": "2 Synonyms: %s, %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 782,
                                            "endIndex": 783,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 782,
                                                        "endIndex": 783,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 783,
                                            "endIndex": 784,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 783,
                                                        "endIndex": 784,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 784,
                                            "endIndex": 785,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 784,
                                                        "endIndex": 785,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 785,
                                            "endIndex": 786,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 785,
                                                        "endIndex": 786,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 786,
                                            "endIndex": 787,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 786,
                                                        "endIndex": 787,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 787,
                                            "endIndex": 788,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 787,
                                                        "endIndex": 788,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 788,
                                            "endIndex": 789,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 788,
                                                        "endIndex": 789,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 789,
                                            "endIndex": 801,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 789,
                                                        "endIndex": 801,
                                                        "textRun": {
                                                            "content": "2 Antonyms: %s, %s\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "startIndex": 801,
                                            "endIndex": 802,
                                            "paragraph": {
                                                "elements": [
                                                    {
                                                        "startIndex": 801,
                                                        "endIndex": 802,
                                                        "textRun": {
                                                            "content": "\n",
                                                            "textStyle": {
                                                                "bold": true,
                                                                "fontSize": {
                                                                    "magnitude": 8,
                                                                    "unit": "PT"
                                                                }
                                                            }
                                                        }
                                                    }
                                                ],
                                                "paragraphStyle": {
                                                    "namedStyleType": "NORMAL_TEXT",
                                                    "alignment": "START",
                                                    "lineSpacing": 100,
                                                    "direction": "LEFT_TO_RIGHT",
                                                    "spacingMode": "COLLAPSE_LISTS",
                                                    "spaceAbove": {
                                                        "unit": "PT"
                                                    },
                                                    "spaceBelow": {
                                                        "unit": "PT"
                                                    },
                                                    "borderBetween": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderTop": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderBottom": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderLeft": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "borderRight": {
                                                        "color": {},
                                                        "width": {
                                                            "unit": "PT"
                                                        },
                                                        "padding": {
                                                            "unit": "PT"
                                                        },
                                                        "dashStyle": "SOLID"
                                                    },
                                                    "indentFirstLine": {
                                                        "unit": "PT"
                                                    },
                                                    "indentStart": {
                                                        "unit": "PT"
                                                    },
                                                    "indentEnd": {
                                                        "unit": "PT"
                                                    },
                                                    "keepLinesTogether": false,
                                                    "keepWithNext": false,
                                                    "avoidWidowAndOrphan": false,
                                                    "shading": {
                                                        "backgroundColor": {}
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "tableCellStyle": {
                                        "rowSpan": 1,
                                        "columnSpan": 1,
                                        "backgroundColor": {},
                                        "borderRight": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "borderBottom": {
                                            "color": {
                                                "color": {
                                                    "rgbColor": {}
                                                }
                                            },
                                            "width": {
                                                "magnitude": 3,
                                                "unit": "PT"
                                            },
                                            "dashStyle": "SOLID"
                                        },
                                        "paddingLeft": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingRight": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingTop": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "paddingBottom": {
                                            "magnitude": 5,
                                            "unit": "PT"
                                        },
                                        "contentAlignment": "TOP"
                                    }
                                }
                            ],
                            "tableRowStyle": {
                                "minRowHeight": {
                                    "magnitude": 178.5,
                                    "unit": "PT"
                                }
                            }
                        }
                    ],
                    "tableStyle": {
                        "tableColumnProperties": [
                            {
                                "widthType": "FIXED_WIDTH",
                                "width": {
                                    "magnitude": 144.75,
                                    "unit": "PT"
                                }
                            },
                            {
                                "widthType": "FIXED_WIDTH",
                                "width": {
                                    "magnitude": 144.75,
                                    "unit": "PT"
                                }
                            },
                            {
                                "widthType": "FIXED_WIDTH",
                                "width": {
                                    "magnitude": 144.75,
                                    "unit": "PT"
                                }
                            },
                            {
                                "widthType": "FIXED_WIDTH",
                                "width": {
                                    "magnitude": 144.75,
                                    "unit": "PT"
                                }
                            }
                        ]
                    }
                }
            },
            {
                "startIndex": 803,
                "endIndex": 804,
                "paragraph": {
                    "elements": [
                        {
                            "startIndex": 803,
                            "endIndex": 804,
                            "textRun": {
                                "content": "\n",
                                "textStyle": {
                                    "bold": true,
                                    "fontSize": {
                                        "magnitude": 12,
                                        "unit": "PT"
                                    }
                                }
                            }
                        }
                    ],
                    "paragraphStyle": {
                        "namedStyleType": "NORMAL_TEXT",
                        "alignment": "START",
                        "direction": "LEFT_TO_RIGHT",
                        "borderBetween": {
                            "color": {},
                            "width": {
                                "unit": "PT"
                            },
                            "padding": {
                                "unit": "PT"
                            },
                            "dashStyle": "SOLID"
                        },
                        "borderTop": {
                            "color": {},
                            "width": {
                                "unit": "PT"
                            },
                            "padding": {
                                "unit": "PT"
                            },
                            "dashStyle": "SOLID"
                        },
                        "borderBottom": {
                            "color": {},
                            "width": {
                                "unit": "PT"
                            },
                            "padding": {
                                "unit": "PT"
                            },
                            "dashStyle": "SOLID"
                        },
                        "borderLeft": {
                            "color": {},
                            "width": {
                                "unit": "PT"
                            },
                            "padding": {
                                "unit": "PT"
                            },
                            "dashStyle": "SOLID"
                        },
                        "borderRight": {
                            "color": {},
                            "width": {
                                "unit": "PT"
                            },
                            "padding": {
                                "unit": "PT"
                            },
                            "dashStyle": "SOLID"
                        },
                        "shading": {
                            "backgroundColor": {}
                        }
                    }
                }
            }
        ]
    },
)
