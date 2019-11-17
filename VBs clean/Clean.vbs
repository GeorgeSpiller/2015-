On Error Resume Next
Set fso = CreateObject("Scripting.FileSystemObject")
Set filesys=CreateObject("Scripting.FileSystemObject")
Const ForReading = 1, ForWriting = 2, ForAppending = 8 
folderpath = "E:\code\Vbs clean\Sandbox"
newfolderpath = folderpath & "\VBs_Clean"
Set directory = fso.GetFolder(".").Files
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFileSys = CreateObject("Scripting.FileSystemObject")


msgbox "This Script sorts out your loose files that are not in a directory" & vbCrLf & "The currant sorting directory is:" & vbCrLf & folderpath & vbCrLf & "To change this, open with notepad and change the folderpath variable on the 5th line"
msgbox "Please see info.txt in: " & vbCrLf & newfolderpath & vbCrLf & " For more details"

If filesys.FolderExists(newfolderpath) Then 'If a folder called all is already there, change the name of the new dir
newfolderpath = folderpath & "\VBs_Clean(2)"
fso.CreateFolder(newfolderpath)
Set MyFile = fso.CreateTextFile(newfolderpath & "\Info.txt", True)
	MyFile.WriteLine("This is a file containnig information on the transfer")
	MyFile.WriteLine("a folder named \VBs_Clean was detected, renamed \VBs_Clean to \VBs_Clean(2)")
	MyFile.Close
End If 

If NOT filesys.FolderExists(newfolderpath) Then 
fso.CreateFolder(newfolderpath)
Set MyFile = fso.CreateTextFile(newfolderpath & "\Info.txt", True)
MyFile.WriteLine("This is a file containnig information on the transfer")
MyFile.Close
end if

result = MsgBox ("do you wish to back up files before starting?", vbYesNo, "Backup")
Select Case result
Case vbYes
    message = "Press ok to start backup, More information on the backup process can be found in info.txt"
	Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
	filetxt.WriteLine("Backup: True")
	filetxt.Close
	call backup
Case vbNo
    message = "backup cancelled"
	Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
	filetxt.WriteLine("Backup: False")
	filetxt.Close
End Select
MsgBox message, vbInformation


msgbox "Clean up started"

Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
	filetxt.WriteLine("==========CLEAN-UP==========")
	filetxt.WriteLine("" & vbCrLf & "The \VBs_Clean directory contains all your files organised into" & vbCrLf & "directorys via file type. This means that folders will not be c" & vbCrlf & "oppied over, only the files."  & vbCrLf & "")
	filetxt.Close
	
objStartFolder = folderpath
Set objFolder = objFSO.GetFolder(folderpath)
Set colFiles = objFolder.Files


For Each objFile in colFiles
	fileExtentions = UCase(objFSO.GetExtensionName(objFile.name))
	If NOT filesys.FolderExists(newfolderpath & "\" & fileExtentions) Then
		fso.CreateFolder(newfolderpath & "\" & fileExtentions)
		Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
		filetxt.WriteLine("A " & fileExtentions & " file was found, folder " & fileExtentions & " created") 
		filetxt.Close
		msgbox "File with extention " & fileExtentions & " found, folder created"
	end if 
	filesys.CopyFile folderpath & "\" & objFile.Name, newfolderpath & "\" & fileExtentions & "\"
	Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
	filetxt.WriteLine("File " & objFile.Name & " coppied to " & fileExtentions)
	filetxt.WriteLine("File " & objFile.Name & " deleated from parent dir")
	filesys.DeleteFile folderpath & "\" & objFile.Name
	filetxt.Close

Next



sub backup:
	If Err.Number <> 0 Then backuperror

	set filesys=CreateObject("Scripting.FileSystemObject")
	'Testing if the back up folder already exists
	backupdir = folderpath & "\BACKUP"
	If filesys.FolderExists(folderpath & "\BACKUP") Then 'If a folder called all is already there, change the name of the new dir
	backupdir = folderpath & "\BACKUP(2)"
	Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
		filetxt.WriteLine("a folder named \BACKUP was detected, renamed \BACKUP to \BACKUP(2)")
		filetxt.Close
	fso.CreateFolder(backupdir)
	End If 
	If NOT filesys.FolderExists(folderpath & "\BACKUP") Then 
	fso.CreateFolder(backupdir)
	end if

	objStartFolder = folderpath
	Set objFolder = objFSO.GetFolder(folderpath)
	Set colFiles = objFolder.Files

	Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
		filetxt.WriteLine("==========BACKUP==========")
		filetxt.WriteLine("" & vbCrLf & "The backup directory contains all your files how they where arra" & vbCrLf & "nged originaly. Thease file will not be sorted into directorys"  & vbCrLf & "")
		filetxt.Close

	For Each objFile in colFiles
		filesys.CopyFile folderpath & "\" & objFile.Name, backupdir
		Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
		filetxt.WriteLine("File " & objFile.Name & " coppied to " & backupdir)
		filetxt.Close
	Next

	Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
		filetxt.WriteLine("" & vbCrLf)
		filetxt.Close
	'================CODE WITH COPPY ERROR================'
	'													  '
	'dim filesys 										  '
	'set filesys=CreateObject("Scripting.FileSystemObject") 
	'If filesys.FolderExists(folderpath & "\BACKUP") Then '
	'filesys.CopyFolder folderpath, folderpath & "\BACKUP\" 
	'End If 											  '
	'													  '
	'msgbox "the script will now quit"					  '
	'Wscript.Quit										  '
	'end sub											  '
	'====================================================='
	end sub

	sub backuperror
	Set filetxt = filesys.OpenTextFile(newfolderpath & "\Info.txt", ForAppending, True) 
	filetxt.WriteLine("" & vbCrLf & "There is an error with sub backup. Copys of your original layout" & vbCrLf & "where unable to be made. This may be due to copy commands unable" & vbCrLf & "to coppy folders with files in. However, this program does not d" & vbCrLf & "eleat any files, only copys them, so they would still be safe if" & vbCrLf & "you were to go ahead with the script.")
	filetxt.WriteLine("")
	filetxt.Close
	backuperrorresult = msgbox ("There was a copy error, see info.txt in VBs_Clean for more details" & vbCrLf &  "do you wish to continue with the script", vbYesNo, "Backup error")
	Select Case backuperrorresult
	Case vbYes
	   exit sub
	Case vbNo
	   Wscript.Quit
	End Select
	msgbox "The code will now stop"
	Wscript.Quit
end sub


msgbox "Compleate"