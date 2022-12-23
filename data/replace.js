/*   <action jsname="action_replace" description="Replace current scene node with a different scene node">
     <property name="ReplacementNode" type="scenenode" />      
     </action>
*/

action_replace = function() {};

action_replace.prototype.execute = function(currentNode) {

var curPos = ccbGetSceneNodeProperty(currentNode, "Position");
var sourceNode = this.ReplacementNode;
var newscenenode = ccbCloneSceneNode(sourceNode);
ccbSetSceneNodeProperty(newscenenode, "Name", "replacer");
ccbSetSceneNodeProperty(newscenenode, "Visible", true);
ccbSetSceneNodeProperty(newscenenode,"Position",curPos);
ccbRemoveSceneNode(currentNode);
};