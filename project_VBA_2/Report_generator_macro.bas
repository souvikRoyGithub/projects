Attribute VB_Name = "Module2"
'Only Run the "report_generator" macro

Public Sub report_generator()

Dim i As Integer
i = 1
Worksheets("All Portfolios").Activate
[a1].Select
Selection.Interior.Color = RGB(250, 191, 143)
Selection.Offset(1, 0).Select
Selection.Interior.Color = RGB(177, 160, 199)
[b4].Select
Selection.Interior.Color = RGB(217, 217, 217)
For i = 1 To (Worksheets.Count - 1)
    Worksheets("All Portfolios").Activate
    Cells(82000, 2).Select
    Selection.End(xlUp).Select
    Selection.Offset(2, 0).Select
    Selection.Value = Worksheets(i).Name & " portfolio"
    Selection.Interior.Color = RGB(216, 228, 188)
    Selection.Font.Bold = True
    Selection.Offset(2, 0).Select
    Selection.Value = "Symbol"
    Selection.Interior.Color = RGB(242, 220, 219)
    Selection.Font.Bold = True
    Selection.Offset(0, 1).Select
    Selection.Value = "Open"
    Selection.Interior.Color = RGB(242, 220, 219)
    Selection.Font.Bold = True
    Selection.Offset(0, 1).Select
    Selection.Value = "Close"
    Selection.Interior.Color = RGB(242, 220, 219)
    Selection.Font.Bold = True
    Selection.Offset(0, 1).Select
    Selection.Value = "Net charge"
    Selection.Interior.Color = RGB(242, 220, 219)
    Selection.Font.Bold = True
    Selection.Offset(1, -3).Select
    Worksheets(i).Activate
    [a1].Select
    Selection.CurrentRegion.Select
    Selection.Copy
    Worksheets("All Portfolios").Activate
    ActiveSheet.PasteSpecial
    Call test_coloring
    Next i
[a3].Select
Call auto_format
    
End Sub

Sub test_coloring()
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .ThemeColor = xlThemeColorAccent1
        .TintAndShade = 0.599993896298105
        .PatternTintAndShade = 0
    End With
End Sub


Public Sub auto_format()
    Columns("A:A").EntireColumn.AutoFit
    Columns("B:B").EntireColumn.AutoFit
    Columns("C:C").EntireColumn.AutoFit
    Columns("D:D").EntireColumn.AutoFit
    Columns("E:E").EntireColumn.AutoFit
End Sub
