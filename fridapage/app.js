require.config({ paths: { 'vs': './node_modules/monaco-editor/min/vs' } });
require(['vs/editor/editor.main'], function () {

    // 初始化变量
    var defaultCode = [
        'Java.perform(function(){',
        '      console.log("succsess");',
        '})'
    ].join('\n');
	
    // 定义编辑器主题
    // monaco.editor.defineTheme('myTheme', {
    //     base: 'vs',
    //     inherit: true,
        // rules: [{ background: 'EDF9FA' }],
        // colors: { 'editor.lineHighlightBackground': '#0000FF20' }
    // });
    // monaco.editor.setTheme('myTheme');
    // 新建一个编辑器
    function newEditor(container_id, code, language) {
        var model = monaco.editor.createModel(code, language);
        var editor = monaco.editor.create(document.getElementById(container_id), {
            model: model,
	        automaticLayout: true
        });
        return editor;
    }

    // 新建一个 div
    function addNewEditor(code, language) {
        var new_container = document.createElement("DIV");
        new_container.id = "container-0";
        new_container.className = "container";
        document.getElementById("root").appendChild(new_container);
        return newEditor(new_container.id, code, language);
    }

    window.fridaEditor = addNewEditor(defaultCode, 'typescript');

    
});