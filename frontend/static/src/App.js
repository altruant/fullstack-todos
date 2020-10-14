import React from 'react';
import TodoList from './components/TodoList.js'
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      tasks: [],
    }
  }

  componentDidMount(){
    console.log('here');
    fetch('/api/v1/')
      .then(response => response.json())
      .then(data => this.setState({ tasks: data }))
      .catch(error => console.log('Error', error))
  }
  render() {
    return (
      <div>
        <TodoList tasks={this.state.tasks} />
      </div>
    );
  }
}

export default App;
