Attribute VB_Name = "Module3"
'Only run "sortby_userinput" macro


Public Sub sort_by_date_time()
    ActiveWorkbook.Worksheets("Quarter 1").Sort.SortFields.Clear
    ActiveWorkbook.Worksheets("Quarter 1").Sort.SortFields.Add2 Key:=Range( _
        "A5:A78"), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
    ActiveWorkbook.Worksheets("Quarter 1").Sort.SortFields.Add2 Key:=Range( _
        "B5:B78"), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
    With ActiveWorkbook.Worksheets("Quarter 1").Sort
        .SetRange Range("A4:G78")
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With
    ActiveWindow.SmallScroll Down:=-12
End Sub

Public Sub sort_by_rep_client()
    ActiveWorkbook.Worksheets("Quarter 1").Sort.SortFields.Clear
    ActiveWorkbook.Worksheets("Quarter 1").Sort.SortFields.Add2 Key:=Range( _
        "C5:C78"), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
    ActiveWorkbook.Worksheets("Quarter 1").Sort.SortFields.Add2 Key:=Range( _
        "D5:D78"), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
    With ActiveWorkbook.Worksheets("Quarter 1").Sort
        .SetRange Range("A4:G78")
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With
End Sub

Public Sub sortby_userinput()
Dim msg, titlebar_txt, default_txt, strresponse, strresponse2, msg2 As String
Dim intresponse As Integer
msg = "How you want to sort your data:" & vbCrLf & _
"Enter 1 for Date and then Time or Enter 2 for Rep and then client"
titlebar_txt = "sort"
msg2 = "You have'nt enter 1 or 2,you wanna try again?"
default_txt = "Enter 1 or 2"
strresponse = InputBox(msg, titlebar_txt, default_txt)
If strresponse = "1" Then
    Call sort_by_date_time
ElseIf strresponse = "2" Then
    Call sort_by_rep_client
Else
    strresponse2 = MsgBox(msg2, vbYesNo, "Response from computer")
    If strresponse2 = vbYes Then
        Call sortby_userinput
    End If
End If

End Sub
