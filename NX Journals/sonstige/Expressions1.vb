Option Strict Off
Imports System
Imports NXOpen
 
Module NXJ_Exp_1
 
    Sub Main()
 
        Dim theSession As Session = Session.GetSession()
	   Dim workPart As NXOpen.Part = theSession.Parts.Work
	   Dim mmUnit As NXOpen.Unit = workPart.UnitCollection.GetBase("Length") 
		Dim cmUnit As NXOpen.Unit = workPart.UnitCollection.FindObject("CentiMeter") 
		
		For Each exp As NXOpen.Expression In workPart.Expressions 
			if exp.Name = "diameter"
				
				exp.value = "22"
				
				
			
				
			end if
		next

		theSession.UpdateManager.DoUpdate(1)
		
		

	End Sub 
End Module










