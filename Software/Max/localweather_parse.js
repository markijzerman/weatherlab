autowatch = 1;

var myDict = new Dict("localWeatherstation");


function parseDict()
{
	var dataAsString = myDict.get("body");

	var parsedDictLocal = new Dict("parsedDictLocal");

	parsedDictLocal.parse(dataAsString);

	outlet(0, parsedDictLocal.name);
}