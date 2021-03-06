'NXJournaling.com
'NXOpen ListingWindow
'write to text file example
 
Option Strict Off
Imports System
Imports NXOpen
 
Module Module1
 
    Sub Main()
 
        Dim theSession As Session = Session.GetSession()
        Dim workPart As Part = theSession.Parts.Work
        Dim lw As ListingWindow = theSession.ListingWindow
        Dim myDocs As String
        myDocs = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Dim outputFile As String = "C:\Users\Marcel\Google Drive\Masterthesis\TOOLS\expressions.txt"
 
        'get information about current work part
        Dim fileName As String = IO.Path.GetFileName(workPart.FullPath)
        Dim fileNameNoExt As String = IO.Path.GetFileNameWithoutExtension(workPart.FullPath)
        Dim parentFolder As String = IO.Path.GetDirectoryName(workPart.FullPath)
        Dim root As String = IO.Path.GetPathRoot(workPart.FullPath)
 
        '***** comment out this section to append to existing file *****
        'does file already exist? if so, delete it
        If IO.File.Exists(outputFile) Then
            Try
                IO.File.Delete(outputFile)
            Catch ex As Exception
                MsgBox(ex.Message, MsgBoxStyle.OkOnly, "Error deleting file:")
            End Try
        End If
        '***** end of section *****
 
        'use listing window to write to file and window
        lw.SelectDevice(ListingWindow.DeviceType.FileAndWindow, outputFile)
        lw.Open()

 	  'hier steht der text
        Const undoMarkName As String = "NXJ query expressions"
        Dim markId1 As Session.UndoMarkId
        markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, undoMarkName)
 
        For Each temp As Expression In workPart.Expressions
            'lw.WriteLine("name: " & temp.Name)
            

            Select Case temp.Type
                Case Is = "Number"
                    Try
                    	   lw.WriteLine(temp.equation)
				Catch ex As NullReferenceException
                        lw.WriteLine("expression is constant (unitless)")
                    Catch ex2 As Exception
                        lw.WriteLine("!! error: " & ex2.Message)
                    End Try
 
                Case Is = "String"
                    lw.WriteLine("string value: " & temp.StringValue)
 
                Case Is = "Integer"
 				lw.WriteLine(temp.equation)

                 
                Case Is = "Point"
                    lw.WriteLine("point value: " & temp.PointValue.ToString)
 

 
                Case Else
                    lw.WriteLine("Type: " & temp.Type & " is not handled by this journal")
 
            End Select

             
            'lw.WriteLine("")
        Next
 
       
        lw.Close()
        'flush file buffer by changing listing window device
        lw.SelectDevice(ListingWindow.DeviceType.Window, "")
	  
		 

    End Sub
 
End Module










