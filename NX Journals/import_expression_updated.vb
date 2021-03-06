' NX 12.0.0.27
' Journal created by spacefactory on Mon Feb 24 11:20:20 2020 Mitteleuropäische Zeit

'
Imports System
Imports NXOpen

Module NXJournal
Sub Main (ByVal args() As String) 

Dim theSession As NXOpen.Session = NXOpen.Session.GetSession()
Dim workPart As NXOpen.Part = theSession.Parts.Work

Dim displayPart As NXOpen.Part = theSession.Parts.Display

' ----------------------------------------------
'   Menu: Tools->Expressions...
' ----------------------------------------------
theSession.Preferences.Modeling.UpdatePending = False

Dim markId1 As NXOpen.Session.UndoMarkId = Nothing
markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")

theSession.SetUndoMarkName(markId1, "Expressions Dialog")

Dim markId2 As NXOpen.Session.UndoMarkId = Nothing
markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Import Expressions")

Dim expModified1 As Boolean = Nothing
Dim errorMessages1() As String
workPart.Expressions.ImportFromFile("C:\Users\Marcel\Google Drive\Masterthesis\TOOLS\expression_updated.exp", NXOpen.ExpressionCollection.ImportMode.Replace, expModified1, errorMessages1)

Dim markId3 As NXOpen.Session.UndoMarkId = Nothing
markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")

Dim markId4 As NXOpen.Session.UndoMarkId = Nothing
markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Make Up to Date")

Dim markId5 As NXOpen.Session.UndoMarkId = Nothing
markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "NX update")

Dim nErrs1 As Integer = Nothing
nErrs1 = theSession.UpdateManager.DoUpdate(markId5)

theSession.DeleteUndoMark(markId5, "NX update")

theSession.DeleteUndoMark(markId4, Nothing)

theSession.DeleteUndoMark(markId3, Nothing)

theSession.SetUndoMarkName(markId1, "Expressions")

theSession.DeleteUndoMark(markId2, Nothing)

Dim markId6 As NXOpen.Session.UndoMarkId = Nothing
markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")

theSession.SetUndoMarkName(markId6, "Expressions Dialog")

' ----------------------------------------------
'   Dialog Begin Expressions
' ----------------------------------------------
Dim markId7 As NXOpen.Session.UndoMarkId = Nothing
markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")

theSession.DeleteUndoMark(markId7, Nothing)

Dim markId8 As NXOpen.Session.UndoMarkId = Nothing
markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")

Dim markId9 As NXOpen.Session.UndoMarkId = Nothing
markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Make Up to Date")

Dim markId10 As NXOpen.Session.UndoMarkId = Nothing
markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "NX update")

Dim nErrs2 As Integer = Nothing
nErrs2 = theSession.UpdateManager.DoUpdate(markId10)

theSession.DeleteUndoMark(markId10, "NX update")

theSession.DeleteUndoMark(markId9, Nothing)

theSession.DeleteUndoMark(markId8, Nothing)

theSession.SetUndoMarkName(markId6, "Expressions")

Dim scaleAboutPoint1 As NXOpen.Point3d = New NXOpen.Point3d(19.607991658715793, 22.897923145077574, 0.0)
Dim viewCenter1 As NXOpen.Point3d = New NXOpen.Point3d(-19.607991658716035, -22.897923145077652, 0.0)
workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)

Dim scaleAboutPoint2 As NXOpen.Point3d = New NXOpen.Point3d(25.167975870667107, 28.622403931346991, 0.0)
Dim viewCenter2 As NXOpen.Point3d = New NXOpen.Point3d(-25.167975870667338, -28.622403931347023, 0.0)
workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint2, viewCenter2)

Dim origin1 As NXOpen.Point3d = New NXOpen.Point3d(34.9176528465416, 35.874880238953068, -6.4991116750423288)
workPart.ModelingViews.WorkView.SetOrigin(origin1)

Dim origin2 As NXOpen.Point3d = New NXOpen.Point3d(34.9176528465416, 35.874880238953068, -6.4991116750423288)
workPart.ModelingViews.WorkView.SetOrigin(origin2)

' ----------------------------------------------
'   Menu: Tools->Journal->Stop Recording
' ----------------------------------------------

End Sub
End Module


