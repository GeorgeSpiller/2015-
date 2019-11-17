Set WshShell = WScript.CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

strDesktop = WshShell.SpecialFolders("Desktop")
rootDskPath = "D:\Documents\Code\VBS\[VBS] complete\Toggle Dsk"
DskPresetPath = rootDskPath & "\Dsktp_Presets"
info_dir = rootDskPath & "\info.txt"
Dsk1Path = DskPresetPath & "\DSK_1"
Dsk2Path = DskPresetPath & "\DSK_2"


'Check if both desktop folders exist:
'Desktop Presets validation:
Set Folder = fso.GetFolder(DskPresetPath)
dsk_num = 0
For Each Subfolder in Folder.SubFolders
    'Wscript.Echo Subfolder.Name
	dsk_num = dsk_num + 1
Next

if dsk_num > 1 then
else
	msgbox("incorrect number of Desktop Presets")
	WScript.Quit 1
end if 

'Check if info.txt exists
'Read info.txt

If fso.FileExists(info_dir) Then 
	Set infotxt = fso.OpenTextFile(info_dir, 1)
		info_txt_raw = infotxt.ReadAll
	infotxt.Close
else 
	msgbox("info text file does not exist at " & vbCrLf & info_dir)
end if
infotxt_array = Split(info_txt_raw, "=")
currentdsk_num = infotxt_array(1)



'Coppying and Moving of items on the desktop
saveCurrentDesktop(currentdsk_num)
loadNextDesktop(currentdsk_num)

'open hta message box:
Const SHOW_ACTIVE_APP = 1 
Set objShell = Wscript.CreateObject("Wscript.Shell") 
objShell.Run ("DesktopMessage.hta"), SHOW_ACTIVE_APP, True 
Wscript.Quit



sub saveCurrentDesktop(dsknum)

	if dsknum = 0 then
	CurrentDskSavePath = Dsk1Path
	else
	CurrentDskSavePath = Dsk2Path
	end if 

	set objCurrentDskSavePath = fso.GetFolder(CurrentDskSavePath)
	'get current desktop info
	Set Folder = fso.GetFolder(WshShell.SpecialFolders("Desktop"))
	Set colFiles = Folder.Files
	'itterate through files, coppy and delete
	
	
	arr_loadOrder = Array("Toggle Desktop","shutdown","Restart Hub","Bitdefender","Documents","Code","Projects","Application Shortcuts", "desktop")
	For Each objFile in colFiles
	fileIsConst = False
		for each arr_files in arr_loadOrder
			sanVal_arr = LCase(CStr(arr_files))
			sanVal_file = LCase(CStr(split(objFile.Name, ".")(0)))
			if StrComp(sanVal_arr, sanVal_file) = 0 then
				fileIsConst = True
			end if 
		next
		if fileIsConst = True then
		else
			fso.MoveFile objFile.Path, objCurrentDskSavePath & "\"
		end if 
	Next

end sub

sub loadNextDesktop(dsknum)

	if dsknum = 0 then
	NextDskSavePath = Dsk2Path
	dsknum = 1
	else
	NextDskSavePath = Dsk1Path
	dsknum = 0
	end if 

	set objNextDskSavePath = fso.GetFolder(NextDskSavePath)
	'get next desktop info
	Set DskFolder = fso.GetFolder(WshShell.SpecialFolders("Desktop"))
	Set colFiles = objNextDskSavePath.Files
	
	'itterate through files, coppy to desktop

	For Each objFile in colFiles
		If fso.FileExists(DskFolder & "\" & objFile.Name) Then 
		else
			fso.MoveFile objFile.Path, DskFolder & "\"
		end if
	Next
	
	'Update info.txt
	Set infotxt = fso.OpenTextFile(info_dir, 2, True) 
	infotxt.WriteLine("current_desktop=" & dsknum)
	infotxt.Close
end sub






