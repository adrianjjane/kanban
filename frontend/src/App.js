import { Switch, Route } from 'react-router-dom';
import './App.css';
import Login from './components/Login';

export default function App() {
  return (
    <div>
      <Switch>
        <Route path="/login">
          <Login />
        </Route>
      </Switch>
    </div>
  );
}
