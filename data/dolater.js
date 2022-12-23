// This is a scripted coppercube action.
// It does an action somewhen later.

/*
	<action jsname="action_DoLater" description="Do something later">
	<property name="TimeMs" type="int" default="500" />
	<property name="ActionToDo" type="action" />
	</action>
*/

action_DoLater = function() {};

// called when the action is executed 
action_DoLater.prototype.execute = function(currentNode)
{
	var me = this; 
	this.registeredFunction = function() { me.doLaterFunc(); }; 
	ccbRegisterOnFrameEvent(me.registeredFunction);	
	this.startTime = (new Date()).getTime();
	this.endTime = this.startTime + this.TimeMs;
	this.currentNode = currentNode;
}


action_DoLater.prototype.doLaterFunc = function()
{
	var now = (new Date()).getTime();
	if (now > this.endTime) {
		ccbInvokeAction(this.ActionToDo, this.registeredFunction);
		ccbUnregisterOnFrameEvent(this.registeredFunction);
							}
}
