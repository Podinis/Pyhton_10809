; Script de Instalação para o Dashboard Gapminder
[Setup]
AppName="Dashboard Gapminder"
AppVersion=1.0
DefaultDirName={pf}\DashboardGapminder
DefaultGroupName=Dashboard Gapminder
UninstallDisplayIcon={app}\app.exe
OutputDir=dist_instalador
OutputBaseFilename=DashboardGapminderSetup
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Dashboard Gapminder"; Filename: "{app}\app.exe"
Name: "{commondesktop}\Dashboard Gapminder"; Filename: "{app}\app.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar atalho no ambiente de trabalho"; GroupDescription: "Opções adicionais"

[Run]
Filename: "{app}\app.exe"; Description: "Executar o Dashboard Gapminder"; Flags: nowait postinstall skipifsilent