Attribute VB_Name = "Module1"
'***ONLY RUN THE "All_merged" MACRO***

Public Sub Insert_text()
Attribute Insert_text.VB_ProcData.VB_Invoke_Func = " \n14"
    [b7].Select
    Selection.CurrentRegion.Select
    Selection.Interior.Color = RGB(255, 255, 102)
    Rows("7:7").Insert
    [b7].Value = "Symbol"
    Range("C7").Value = "Open"
    Range("D7").Value = "Close"
    Range("E7").Value = "Net Charge"
    Range("B4").Value = ActiveSheet.Name & " Portfolio"
    Range("A1").Value = "Our Global Company"
    Range("A2").Value = "Stock prices"
    Range("G1").Select
End Sub
Public Sub format_fonts()
Attribute format_fonts.VB_ProcData.VB_Invoke_Func = " \n14"
    Range("A1").Select
    Selection.Font.Bold = True
    Range("A2").Select
    Selection.Font.Bold = True
    Range("B4").Select
    Selection.Font.Bold = True
    Range("B7").Select
    Selection.Font.Bold = True
    Range("C7").Select
    Selection.Font.Bold = True
    Range("D7").Select
    Selection.Font.Bold = True
    Range("E7").Select
    Selection.Font.Bold = True
    Range("A1").Select
    With Selection.Font
        .Size = 20
    End With
    Range("A2").Select
    With Selection.Font
        .Size = 18
    End With
    Range("B4").Select
    With Selection.Font
        .Size = 16
    End With
    Cells.Select
    With Selection.Font
        .Name = "Verdana"
    End With
    Range("G1").Select
End Sub
Public Sub Color_formating()
Attribute Color_formating.VB_ProcData.VB_Invoke_Func = " \n14"
    
    Range("A1").Font.Color = RGB(226, 107, 10)
    Range("A2").Font.Color = RGB(49, 134, 152)
    Range("B4").Font.Color = RGB(96, 73, 122)
    Range("B7:E7").Interior.Color = RGB(141, 180, 226)
    Range("G1").Select
End Sub
Public Sub last_formatting()
Attribute last_formatting.VB_ProcData.VB_Invoke_Func = " \n14"
    Columns("A:A").EntireColumn.AutoFit
    Columns("B:B").EntireColumn.AutoFit
    Columns("C:C").EntireColumn.AutoFit
    Columns("D:D").EntireColumn.AutoFit
    Columns("E:E").EntireColumn.AutoFit
End Sub

Public Sub All_merged()
    Call Insert_text
    Call Color_formating
    Call format_fonts
    Call last_formatting
End Sub
