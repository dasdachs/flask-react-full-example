import { useEffect, useState } from "react";
import { List } from "../interfaces/Api";

export function PublicLists() {
  const [lists, setLists] = useState<List[]>([]);

  useEffect(() => {
    fetch("/lists/public")
      .then((data) => data.json())
      .then((lists) => setLists(lists));
  }, [setLists]);

  return (
    <table className="table table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">List Name</th>
        </tr>
      </thead>
      <tbody>
        {lists.length === 0 && <div>No public lists</div>}
        {lists.length &&
          lists.map((list) => (
            <tr key={list.id}>
              <th scope="row">{list.id}</th>
              <td>{list.name}</td>
            </tr>
          ))}
      </tbody>
    </table>
  );
}
