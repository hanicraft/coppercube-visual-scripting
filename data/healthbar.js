/*
<action jsname="action_healthbar" description="Health Bar: changes the scale of 2D overlay according to health">
	<property name="Healthbar_Node" type="scenenode"/>
	<property name="Shrink_Multiplier" type="int" default="0.25"/>
	<property name="Health_Variable" type="string" default="#plr.health"/>
</action>
*/

action_healthbar = function()
{
};

action_healthbar.prototype.execute=function(currentNode)
{
var OriginalWidth = ccbGetSceneNodeProperty(this.Healthbar_Node, "Width (percent)");
var banana = ccbGetCopperCubeVariable(this.Health_Variable);
ccbSetSceneNodeProperty(this.Healthbar_Node, "Width (percent)", banana * this.Shrink_Multiplier);
}