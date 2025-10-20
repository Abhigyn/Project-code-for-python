; Inno Setup Script for Calculator App

[Setup]
AppName=Calculator
AppVersion=1.0
AppPublisher=Abhigyan Deepak

; Detect system architecture
ArchitecturesInstallIn64BitMode=x64

; Auto-select correct Program Files folder
DefaultDirName={autopf}\Calculator

OutputDir=.
OutputBaseFilename=CalculatorSetup
SetupIconFile=Calculator.ico
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest

; Enable customizable Start Menu folder
DefaultGroupName=Calculator
DisableProgramGroupPage=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
; Optional shortcuts
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional shortcuts:"; Flags: unchecked
Name: "startmenuicon"; Description: "Create a &Start Menu shortcut"; GroupDescription: "Additional shortcuts:"; Flags: unchecked

[Files]
; Only need the exe
Source: "dist\Calculator.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Start Menu shortcut (optional, under custom folder)
Name: "{group}\Calculator"; Filename: "{app}\Calculator.exe"; Tasks: startmenuicon; IconFilename: "{app}\Calculator.exe"

; Desktop shortcut (optional)
Name: "{autodesktop}\Calculator"; Filename: "{app}\Calculator.exe"; Tasks: desktopicon; IconFilename: "{app}\Calculator.exe"

; Uninstaller shortcut (always in Start Menu group, inside chosen folder)
Name: "{group}\Uninstall Calculator"; Filename: "{uninstallexe}"

[Run]
; Run the app after installation
Filename: "{app}\Calculator.exe"; Description: "Launch Calculator"; Flags: nowait postinstall skipifsilent
