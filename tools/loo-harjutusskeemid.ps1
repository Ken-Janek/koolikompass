# Loo algsest arhitektuuriskeemist kolm õppimiseks mõeldud varianti.
$ErrorActionPreference = 'Stop'
$projectDir = Split-Path $PSScriptRoot -Parent
$sourcePath = Join-Path $projectDir 'diagrams/arhitektuur.drawio'

# Leia diagrams.net-i XML-ist elemendi ID järgi kast või ühendus.
function Get-Cell($doc, $id) {
    return $doc.SelectSingleNode("//mxCell[@id='$id']")
}
# Muuda elemendi koordinaate ja mõõtmeid mxGeometry atribuutides.
function Set-Box($doc, $id, $x, $y, $width, $height) {
    $geometry = (Get-Cell $doc $id).SelectSingleNode('mxGeometry')
    foreach ($pair in @(@('x', $x), @('y', $y), @('width', $width), @('height', $height))) {
        $geometry.SetAttribute($pair[0], [string]$pair[1])
    }
}
# Lisa skeemile uus kast ja selle paigutus; parent määrab konteineri.
function Add-Box($doc, $id, $label, $x, $y, $width, $height, $parent = '1') {
    $cell = $doc.CreateElement('mxCell')
    foreach ($pair in @(@('id', $id), @('value', $label), @('vertex', '1'), @('parent', $parent), @('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=16;'))) {
        $cell.SetAttribute($pair[0], $pair[1])
    }
    $geometry = $doc.CreateElement('mxGeometry')
    $geometry.SetAttribute('as', 'geometry')
    $cell.AppendChild($geometry) | Out-Null
    $doc.SelectSingleNode('//root').AppendChild($cell) | Out-Null
    Set-Box $doc $id $x $y $width $height
}
# Ühenduse source ja target viitavad olemasolevate kastide ID-dele.
function Add-Edge($doc, $id, $label, $source, $target, $extraStyle = '') {
    $cell = $doc.CreateElement('mxCell')
    foreach ($pair in @(@('id', $id), @('value', $label), @('edge', '1'), @('parent', '1'), @('source', $source), @('target', $target), @('style', "edgeStyle=orthogonalEdgeStyle;html=1;startArrow=classic;endArrow=classic;fontSize=13;labelBackgroundColor=#ffffff;$extraStyle"))) {
        $cell.SetAttribute($pair[0], $pair[1])
    }
    $geometry = $doc.CreateElement('mxGeometry')
    $geometry.SetAttribute('relative', '1')
    $geometry.SetAttribute('as', 'geometry')
    $cell.AppendChild($geometry) | Out-Null
    $doc.SelectSingleNode('//root').AppendChild($cell) | Out-Null
}
# Salvesta eraldi UTF-8 fail ning vabasta failikirjutaja ka vea korral.
function Save-Diagram($doc, $fileName, $diagramName) {
    $doc.mxfile.diagram.SetAttribute('name', $diagramName)
    $doc.mxfile.diagram.SetAttribute('id', $fileName.Replace('.drawio', ''))
    $settings = New-Object System.Xml.XmlWriterSettings
    $settings.Indent = $true
    $settings.Encoding = New-Object System.Text.UTF8Encoding($false)
    $writer = [System.Xml.XmlWriter]::Create((Join-Path $projectDir "diagrams/$fileName"), $settings)
    try { $doc.Save($writer) } finally { $writer.Dispose() }
}

# Koopia 1: mobiiliklient kasutab uut API-kihti ja olemasolevat äriloogikat.
$mobile = New-Object System.Xml.XmlDocument
$mobile.Load($sourcePath)
(Get-Cell $mobile 'title').SetAttribute('value', 'KooliKompass — mobiilirakenduse lisamine')
Set-Box $mobile 'server' 440 100 440 600
Set-Box $mobile 'views' 30 80 180 100
Set-Box $mobile 'logic' 60 290 320 80
Set-Box $mobile 'orm' 60 450 320 80
Set-Box $mobile 'browser' 60 170 220 100
Set-Box $mobile 'template' 60 30 220 90
Set-Box $mobile 'title' 360 20 770 50
Set-Box $mobile 'db' 940 550 180 120
Set-Box $mobile 'note' 60 740 1060 65
(Get-Cell $mobile 'https').SetAttribute('value', 'HTTPS<br>HTML-vastus')
(Get-Cell $mobile 'https').SetAttribute('style', 'edgeStyle=orthogonalEdgeStyle;html=1;startArrow=classic;endArrow=classic;exitX=1;exitY=0.5;entryX=0;entryY=0.5;fontSize=13;labelBackgroundColor=#ffffff;')
Add-Box $mobile 'api' 'API päringukiht<br>JSON, autentimine,<br>õiguste kontroll' 230 80 180 100 'server'
Add-Box $mobile 'mobile' 'Mobiilirakendus<br>Eraldi kasutajaliides' 940 180 180 100
Add-Edge $mobile 'mobile-api' 'HTTPS / JSON<br>Autentimine' 'mobile' 'api' 'exitX=0;exitY=0.5;entryX=1;entryY=0.5;'
Add-Edge $mobile 'api-logic' 'Samad ärireeglid' 'api' 'logic' 'exitX=0.5;exitY=1;entryX=0.8;entryY=0;'
(Get-Cell $mobile 'e1').SetAttribute('style', 'edgeStyle=orthogonalEdgeStyle;html=1;startArrow=classic;endArrow=classic;exitX=0.5;exitY=1;entryX=0.2;entryY=0;labelBackgroundColor=#ffffff;')
(Get-Cell $mobile 'e4').SetAttribute('style', 'edgeStyle=orthogonalEdgeStyle;html=1;startArrow=classic;endArrow=classic;exitX=0;exitY=0.2;entryX=1;entryY=0.5;labelBackgroundColor=#ffffff;')
(Get-Cell $mobile 'note').SetAttribute('value', 'Uus: mobiiliklient ja API-kiht. Taaskasutus: äriloogika, ORM ning andmebaas.<br>Veeb kasutab HTML-i, mobiil JSON-i. Mõlemad läbivad õiguste kontrolli. Server on endiselt monoliit.')
Save-Diagram $mobile 'arhitektuur-mobiil.drawio' 'Harjutus 1 — mobiilirakendus'

# Koopia 2: sama monoliidi kaks eksemplari; ühine PostgreSQL ja sessioonid.
$scale = New-Object System.Xml.XmlDocument
$scale.Load($sourcePath)
foreach ($id in @('server', 'views', 'logic', 'orm', 'template', 'https', 'e1', 'e2', 'e3', 'e4')) {
    $cell = Get-Cell $scale $id
    $cell.ParentNode.RemoveChild($cell) | Out-Null
}
(Get-Cell $scale 'title').SetAttribute('value', 'KooliKompass — suurema koormuse võimalik lahendus')
Set-Box $scale 'title' 50 25 1070 55
Set-Box $scale 'browser' 50 330 180 100
Set-Box $scale 'db' 940 300 180 170
Set-Box $scale 'note' 50 710 1070 80
(Get-Cell $scale 'db').SetAttribute('value', 'PostgreSQL<br>Ühised andmed<br>Ühised sessioonid')
Add-Box $scale 'balancer' 'Koormusjaotur<br>Jaotab päringud' 310 330 180 100
Add-Box $scale 'server-a' 'Django eksemplar A<br><br>Päringukiht ja HTML-mallid<br>Äriloogika<br>ORM' 590 150 230 190
Add-Box $scale 'server-b' 'Django eksemplar B<br><br>Päringukiht ja HTML-mallid<br>Äriloogika<br>ORM' 590 450 230 190
Add-Edge $scale 'client-lb' 'HTTPS' 'browser' 'balancer' 'exitX=1;exitY=0.5;entryX=0;entryY=0.5;'
Add-Edge $scale 'lb-a' 'Päring / vastus' 'balancer' 'server-a' 'exitX=1;exitY=0.25;entryX=0;entryY=0.5;'
Add-Edge $scale 'lb-b' 'Päring / vastus' 'balancer' 'server-b' 'exitX=1;exitY=0.75;entryX=0;entryY=0.5;'
Add-Edge $scale 'a-db' 'SQL / read' 'server-a' 'db' 'exitX=1;exitY=0.5;entryX=0;entryY=0.25;'
Add-Edge $scale 'b-db' 'SQL / read' 'server-b' 'db' 'exitX=1;exitY=0.5;entryX=0;entryY=0.75;'
(Get-Cell $scale 'note').SetAttribute('value', 'A ja B on sama kihilise monoliidi koopiad, mitte mikroteenused.<br>Esmalt mõõda koormust. Andmebaas võib endiselt olla pudelikael: kontrolli päringuid, indekseid ja ühenduste arvu.')
Save-Diagram $scale 'arhitektuur-koormus.drawio' 'Harjutus 3 — suurem koormus'

# Koopia 3: tehnilised komponendid säilivad; vähendatakse funktsioonide ulatust.
$deadline = New-Object System.Xml.XmlDocument
$deadline.Load($sourcePath)
$deadline.mxfile.diagram.mxGraphModel.SetAttribute('pageHeight', '1050')
(Get-Cell $deadline 'title').SetAttribute('value', 'KooliKompass — lühema tähtaja põhiversioon')
(Get-Cell $deadline 'logic').SetAttribute('value', 'Äriloogika: US-01–US-05<br>Konto, ained, lisamine,<br>nimekiri, tehtuks märkimine')
Set-Box $deadline 'logic' 60 220 320 100
Set-Box $deadline 'note' 80 670 1000 60
(Get-Cell $deadline 'note').SetAttribute('value', 'Tehniline arhitektuur säilib. Muudatus puudutab esimese väljalaske ulatust ja tööde prioriteete.')
Add-Box $deadline 'release-scope' 'Esimesse versiooni: US-01–US-05 (P1).<br>Hiljem: US-06 (P2), US-07 ja US-08 (P3).<br>Alguses poole võrra lühem tähtaeg: 3 nädalat × 10 h = 30 h.<br>Lood 20 h + seadistus 2 h + demo 1 h + puhver 3 h + proovikasutus ja kasutuselevõtt 4 h.<br>Uuenda tahvlil prioriteedid, kaartide pealkirjad ja kirjeldused.' 80 760 1000 180
(Get-Cell $deadline 'release-scope').SetAttribute('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=16;')
Save-Diagram $deadline 'arhitektuur-tahtaeg.drawio' 'Harjutus 2 — lühem tähtaeg'

Write-Output 'Loodud kolm muudetavat harjutusskeemi. Algne skeem on säilinud.'
