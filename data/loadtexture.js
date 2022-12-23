// This is a scripted coppercube action.
// It dynamically loads a texture (from disk or a web server) and sets it as material onto a scene node.
//
/*
	<action jsname="action_LoadTexture" description="Dynamically load a texture">
		<property name="ChangeWhichNode" type="scenenode" />
		<property name="MaterialIndexToChange" type="int" default="0" />
		<property name="TextureToLoad" type="string" />
	</action>
*/

action_LoadTexture = function()
{
};

// called when the action is executed 
action_LoadTexture.prototype.execute = function(currentNode)
{
	var tex = ccbLoadTexture(this.TextureToLoad);
	ccbSetSceneNodeMaterialProperty(this.ChangeWhichNode, this.MaterialIndexToChange, "Texture1", tex);
}